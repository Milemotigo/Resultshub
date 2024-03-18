// // Function to get CSRF token from cookie
// function getCookie(name) {
//     let cookieValue = null;
//     if (document.cookie && document.cookie !== '') {
//         const cookies = document.cookie.split(';');
//         for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === (name + '=')) {
//                 cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//                 break;
//             }
//         }
//     }
//     return cookieValue;
// }



$(document).ready(function() {
    $('#collegesubmit').on('click', function(e) {
        e.preventDefault();
        
        const api_url = 'http://127.0.0.1:8000/';
        const userDetail = $('#inputCredentials').val();
        const password = $('#inputPassword').val();
        // const crsftoken = getCookie('csrftoken');
        console.log(userDetail);
        console.log(password)

        // console.log('Button clicked'); // Add this line for debugging
        alert('Hello');
        const csrfToken = document.querySelector('meta[name="csrf-token"]').getAttribute('content');
        console.log(csrfToken);
        $.ajax({
            url: `${api_url}college/college_login/`,
            type: 'post',

            data: {
                userDetail: userDetail,
                password: password,
            },
            beforeSend: function(xhr) { 
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            },
            success: function(response) {
                alert("Login Successful. Details: " + response.details);
                // window.location.href = api_url + 'college/college_dashboard/';
                window.location.href = `${api_url}college/college_dashboard/`;
            },
            error: function(xhr, errmsg, err) {
                console.log(err.details);
                // alert("Invalid credentials. Please try again.")
                console.log(xhr);
                alert("Error: " + xhr.responseJSON.details);
                console.log(xhr.responseText);
            },
        })
    });
});
