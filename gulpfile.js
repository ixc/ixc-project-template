var gulp  = require('gulp');
var child = require('child_process');

var main = null;

gulp.task('default', ['setup', 'main', 'watch']);

gulp.task('watch', function() {
	gulp.watch('./**/*.py', ['main']);
	gulp.watch('./bower.json', ['setup']);
	gulp.watch('./package.json', ['setup']);
	gulp.watch('./requirements*.txt', ['setup']);
	gulp.watch('./setup.py', ['setup']);
});

gulp.task('setup', function() {
	child.spawnSync('setup-local-dev.sh', {stdio: 'inherit'});
});

gulp.task('main', function() {
	if (main) {
		main.kill();
	}
	main = child.spawn('supervisor.sh', {stdio: 'inherit'});
});
