var gulp  = require('gulp');
var child = require('child_process');

var main = null;

gulp.task('default', ['main', 'watch']);

gulp.task('watch', function() {
	gulp.watch('./**/*.py', ['main']);
	gulp.watch('./bower.json', ['main']);
	gulp.watch('./package.json', ['main']);
	gulp.watch('./requirements*.txt', ['main']);
	gulp.watch('./setup.py', ['main']);
});

gulp.task('main', function() {
	if (main) {
		main.kill();
	}
	main = child.spawn(
		'setup-local-env.sh',
		['migrate.sh', 'supervisor.sh'],
		{stdio: 'inherit'});
});
