let mix = require('laravel-mix');

mix.js('EventixPrj/EventixApp/resources/js/main.js', 'EventixPrj/EventixApp/static/js');
mix.sass('EventixPrj/EventixApp/resources/sass/stylesheet.sass', 'EventixPrj/EventixApp/static/css').options({
    processCssUrls: false
});;