const currentDomain = window.location.origin;

fetch('http://127.0.0.1:8000/csrf_view', {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json',
    },
})
.then(response => {
    if (response.ok) {
        console.log('Запрос успешно выполнен с домена', currentDomain);
    }
    else {
//            alert('Запрос заблокирован политикой CORS для домена:', currentDomain);
        console.log('Запрос заблокирован политикой CORS для домена', currentDomain);
    }
})
.catch(error => {
    console.error('Ошибка при выполнении запроса с домена:', currentDomain, error);
});
