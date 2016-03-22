var gulp  = require('gulp');
var child = require('child_process');

var main = null;

function pipe(result) {
	result.stderr.on('data', function(data) {
		process.stdout.write(data.toString());
	});
	result.stdout.on('data', function(data) {
		process.stdout.write(data.toString());
	});
}

gulp.task('default', ['setup', 'main', 'watch']);

gulp.task('watch', function() {
	gulp.watch('./**/*.py', ['main']);
	gulp.watch('./bower.json', ['setup']);
	gulp.watch('./package.json', ['setup']);
	gulp.watch('./setup.py', ['setup']);
});

gulp.task('setup', function() {
	return child.spawnSync('setup-dev.sh');
});

gulp.task('main', function() {
	if (main) {
		main.kill();
	}
	main = child.spawn('supervisor.sh');
	pipe(main);
});
