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
    $('#collegeLoginForm').on('submit', function(e) {
        e.preventDefault();
        
        const api_url = 'http://127.0.0.1:8000/';
        const userDetail = $('#inputCredentials').val();
        const password = $('#inputPassword').val();
        const crsftoken = getCookie('csrftoken');
        console.log(crsftoken);
        // console.log('Button clicked'); // Add this line for debugging
        alert('Hello');

        $.ajax({
            url: `${api_url}college/college_login/`,
            type: 'post',
            headers: {
                'X-CSRFToken': crsftoken,
            },
            data: {
                userDetail: userDetail,
                password: password,
            },
            success: function(response) {
                console.log(response);
            },
            error: function(xhr, errmsg, err) {
                console.log(err.details);
                alert("Invalid credentials. Please try again.")
            },
        })
    });
});
