let mix = require('laravel-mix');

mix.js('EventixPrj/EventixApp/resources/js/main.js', 'EventixPrj/EventixApp/static/js');
mix.js('EventixPrj/EventixApp/resources/js/xrDemo.js', 'EventixPrj/EventixApp/static/js');

mix.sass('EventixPrj/EventixApp/resources/sass/stylesheet.sass', 'EventixPrj/EventixApp/static/css').options({
    processCssUrls: false
});

mix.sass('EventixPrj/EventixApp/resources/sass/xrDemo.sass', 'EventixPrj/EventixApp/static/css').options({
    processCssUrls: false
});