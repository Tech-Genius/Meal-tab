$(document).ready(function () {
    $(window).load(function() {

        // will first fade out the loading animation 
     
 
         // will fade out the whole DIV that covers the website. 
         $(".ajaxLoader").delay(200).fadeOut("slow");   
 
       }) 
    // $('.ajaxLoader').hide();
    $(".filter-tag").on('click', function () {
        var _filterObj = {};
        $(".filter-tag").each(function (index, ele) {
            var _filterVal = $(this).val();
            var _filterKey = $(this).data('filter');
            _filterObj[_filterKey] = Array.from(document.querySelectorAll('input[data-filter=' + _filterKey + ']:checked')).map(function (el) {
                return el.value;

            });

        });


        $.ajax({
            url: '/filter-category',
            data: _filterObj,
            dataType: 'json',
            beforeSend: function () {
                $('.ajaxLoader').show();
       
                     $(".ajaxLoader").delay(1200).fadeOut("slow");   
             
             
                
            },
            success: function (res) {
                console.log(res)
                $("#product_filtered").html(res.data)
                
            }
        });

    });
});