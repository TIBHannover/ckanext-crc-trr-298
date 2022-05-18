$(document).ready(function(){
    $('#search-type-dropdown').select2({ width: '100%' });

    $('.search-form').submit(function(e){
        e.preventDefault();
        let searchType = $('#search-type-dropdown').val();
        let serachPhrase = $('#field-giant-search-mimic').val();
        if (searchType !== '0'){
            $('#field-giant-search').val('');
            $('#field-giant-search').val(searchType + ":" + serachPhrase);
        }
        $('.search-form')[0].submit();
    });
});