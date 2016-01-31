/*
* Author: 강은석
* Description: Ajax Update with Django
* */

$(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('.like').on('click', function () {
        console.log($(this).val());

        var btn = $(this);

        $.ajax({
            url: "/update/",
            type: 'POST',
            data: {
                object_id: $(this).val()
            },
            success: function (result) {
                console.log(result);
                btn.next().html(result);



            },
            error: function (jqXHR, textStatus, errorThrown) {
                console.log(jqXHR + ", " + textStatus + ", " + errorThrown);
            }
        });
    });

});