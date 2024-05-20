


function submite_login(){
    const email = $("#email").val()
    const password = $("#password").val()
    let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

    var formData = new FormData()
    formData.append('emailId', email)
    formData.append('password', password)
    formData.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
    $.ajax({
        url: '/login/',
        method: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function(response){
            if (response.redirect_url) {
                window.location.href = response.redirect_url;
            } else {
                alert("got error")
            }
            
            
        },
        error: function(response){
            show_error(response.responseJSON['message'])
        }
        
    })
}
