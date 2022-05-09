$(document).ready(function() {
    $('#search-btn').on( 'click', function(e) {
        e.preventDefault();
        let searchText = $('#search-box').val();
        $.ajax( {
            url: '/items?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
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
            error: function(xhr, status, error) {
                console.error(error)
            }
        })
    });
});


