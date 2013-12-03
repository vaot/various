;(function ( $, window, document, undefined ) {

    var pluginName = "slideArrow";

    function slideIt(el, clicked, options){

        var windowWidth = $(window).width(),
            presentationWidth = $(el).width(),
            tempMargin = currentMargin = (windowWidth - presentationWidth)/2,
            currentMargin = (windowWidth - presentationWidth)/2 > 0 ? tempMargin : 0,
            currentEl = $(clicked).position().left,
            elOffsetToContainer = (currentEl - currentMargin) + 50,
            selector = [$(el).attr('id'), "#"] || [$(el).attr('class'), "."],
            elClass = selector[1] + selector[0].split(" ").join(".");

        $(el).css("position","relative");
        $('#slideArrow').text(elClass + ":after{left:" + elOffsetToContainer + "px !important; \
            bottom: 100%; \
            border: solid transparent; \
            content: ''; \
            height: 0; \
            width: 0; \
            position: absolute; \
            pointer-events: none; \
            border-color: rgba(255, 255, 255, 0); \
            border-bottom-color:" + options.coloR + "; \
            border-width: " + options.sizE + "; \
            margin-left: -50px;}"
        );
    }

    function toggleOn(el){
        $($(el).data('toggle-on')).addClass('_current_show_and_hide').show();
        $('_current_show_and_hide').removeClass('_current_show_and_hide').hide();
    }

    $.fn[pluginName] = function(options){

        if ($('#slideArrow').length == 0)
            $("<style type='text/css' id='slideArrow' />").appendTo("head");

        var defaults = $.extend({
            coloR: '#000',
            sizE: '50px',
            bindClickOn: '',
            attachTo: ''
        }, options);

        $(window).on('resize', function(){
            slideArrow(this, '._current_show_and_hide', options);
        });

        return this.each(function(){
            var el = this;
            $(defaults.bindClickOn).on('click', function(){
                slideIt(el, this, defaults);
                if (!typeof $('.anchor').data('toggle-on') == "undefined")
                    toggleOn(this);
            });
            $(defaults.bindClickOn).trigger('click');
        });
    }

})( jQuery, window, document );