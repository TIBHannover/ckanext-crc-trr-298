$(document).ready(function(){
    $('#search-type-dropdown').select2({ width: '100%' });

    $('.search-form').submit(function(e){        
        if($('#search-type-dropdown').length !== 0){
            e.preventDefault();
            let searchType = $('#search-type-dropdown').val();
            let searchPhrase = $('#field-giant-search-mimic').val();
            if (searchType !== '0'){
                $('#field-giant-search').val('');
                $('#field-giant-search').val(searchType + ":" + searchPhrase);
            }
            else{
                $('#field-giant-search').val('');
                $('#field-giant-search').val(searchPhrase);
            }
            $('.search-form')[0].submit();
        }
        else{
            $('.search-form')[0].submit();        
        }        
    });
});