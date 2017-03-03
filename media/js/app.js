$('#form-container form').on('submit', function (e) {
    e.preventDefault();
    var datum = {}
    var $sections = $(this).find('fieldset');
    $sections.each(function () {
        var sectionKey = $(this).data().key;
        datum[sectionKey] = {};
        var $inputs = $(this).find($('input, textarea, select'));
        $inputs.each(function () {
            var attr = $(this).data().key;
            var val = $(this).val();
            var type = $(this).attr('type') || $(this).data().type;
            if(type && type === 'number')
                val = parseInt(val);
            datum[sectionKey][attr] = val;
        })
    });

    var postUrl = "/api/loan/";
    $.ajax({
        url: postUrl,
        type: "POST",
        data: JSON.stringify(datum),
        contentType: "application/json",
    });
})