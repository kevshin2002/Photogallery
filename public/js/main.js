document.addEventListener("DOMContentLoaded", function() {
    
});

function server_request(url, data={}, verb='GET', callback) {
    return fetch(url, {
        credentials: 'same-origin',
        method: verb,
        body: verb !== 'GET' ? JSON.stringify(data) : null, // Don't send body for GET requests
        headers: {'Content-Type': 'application/json'}
    })
    .then(response => response.json())
    .then(response => {
        if(callback) callback(response);
    })
    .catch(error => console.error('Error:', error));
}
