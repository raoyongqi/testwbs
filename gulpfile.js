const gulp = require('gulp');
const fileInclude = require('gulp-file-include');  // 引入 gulp-file-include 插件
const fs = require('fs');
const path = require('path');

// 定义合并 HTML 的任务
gulp.task('merge-html', function() {
  return gulp.src([
    'C:/Users/r/Desktop/test_webofsci/test_webofsci/ConvolutionalNeuralNetworks_1.html',
    'C:/Users/r/Desktop/test_webofsci/test_webofsci/ConvolutionalNeuralNetworks_2.html',
    'C:/Users/r/Desktop/test_webofsci/test_webofsci/ConvolutionalNeuralNetworks_3.html'
  ]) // 输入文件路径
    .pipe(fileInclude({
      // 包括 HTML 文件内容
      prefix: '@@',
      basepath: '@file'
    }))
    .pipe(gulp.dest('C:/Users/r/Desktop/test_webofsci/test_webofsci/combined.html'));  // 输出路径
});

// 默认任务
gulp.task('default', gulp.series('merge-html'));
