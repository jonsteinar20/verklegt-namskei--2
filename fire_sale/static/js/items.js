//import * as name from "../../item"

$(document).ready(function() {
    $('#search-btn').on('click', function (e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        $.ajax({
            url: '/items?search_filter=' + searchText,
            type: 'GET',
            success: function (resp) {
                let newHtml = resp.data.map(d => {
                    return `<div class="well item">
                                <a href="/items/$(d.id)">
                                    <img class="item-img" src="${d.firstImage}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                            </div>`
                });
                $('.items').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function (xhr, status, error) {
                console.error(error)
            }
        })
    });
});

$('#orderby').change(function(e) {
    let filter_by = $('#orderby').val()
    if(filter_by == 'Name') {
        filter_by_name()
        console.log("name")
    }
    else {
        console.log("price")
        //item.views.filter_by_price()
    }
})


