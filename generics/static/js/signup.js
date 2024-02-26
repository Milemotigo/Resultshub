// Function to get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}



$(document).ready(function() {
    $('#collegeSignUpForm').on('submit', function(e) {
        e.preventDefault();
        
        const api_url = 'http://127.0.0.1:8000/';
        const crsftoken = getCookie('csrftoken');
        const email = $('#email').val();
        const college_name = $('#college_name').val();
        const username = $('#username').val();
        const password = $('#password').val();

        // alert('Hello');

        $.ajax({
            url: `${api_url}college/college_signup/`,
            type: 'post',
            headers: {
                'X-CSRFToken': crsftoken,
            },
            data: {
                email: email,
                college_name: college_name,
                username: username,
                password: password,
            },
            success: function(response) {
                console.log(response);
                window.location.href = `${api_url}generics/login/`;
                alert(response);
            },
            error: function(xhr, errmsg, err) {
                console.log(err);
                console.log(JSON.stringify(xhr.responseJSON));
                alert("error signing up. Please try again.")
            },
        })
    });
});
