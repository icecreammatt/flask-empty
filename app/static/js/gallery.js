$(document).ready(function() {
    "use strict";

    var gallery = function() {
        var imageBorder = 50;
        var $imageOri = $('img'),
            imageWidth = $imageOri.width(),
            imageHeight = $imageOri.height();

        var resizeImage = function($image) {
            if(typeof($image) != jQuery) {
                $image = $($image);
            }

            var windowWidth = $(window).width(),
                windowHeight = $(window).height();

            if($image.width() >= windowWidth) {
                $image.width(windowWidth * .8);
            }
            if($image.height() >= windowHeight) {
                $image.height(windowHeight * .8);
            }
        };

        var hideChrome = function($image) {
            if(typeof($image) != jQuery) {
                $image = $($image);
            }

            $image.click(function(){
                location.href = $image.attr('src');
            });
        };

        resizeImage($imageOri);
        hideChrome($imageOri);

        return {
            resize: resizeImage
        };
    }();

    $(window).resize(function(){
        gallery.resize('img');
    });
});