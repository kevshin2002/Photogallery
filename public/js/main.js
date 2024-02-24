document.addEventListener("DOMContentLoaded", function() {
    
    // Handle creation of a new image
    document.getElementById('createForm').addEventListener('submit', function(e) {
        e.preventDefault();
        const title = document.getElementById('createImgTitle').value;
        const description = document.getElementById('createImgDescription').value;
        const src = document.getElementById('createImgSrc').value;
        server_request('/images', { title, description, src }, 'POST', function(response) {
          //  console.log(response);
          //  window.location.reload(); 
          //  Fix this so that it renders image without reloading
        });
    });

    // Event delegation for modify and delete buttons
    document.getElementById('imagesList').addEventListener('click', function(e) {
        const form = e.target.closest('form');
        if (!form) return; // Exit if the click wasn't on a form or within a form
        const imgId = form.getAttribute('data-img-id');
        
        if (e.target.classList.contains('modifyBtn')) {
            const formData = new FormData(form);
            const title = formData.get('title');
            const description = formData.get('description');
            server_request(`/${imgId}`, { title, description }, 'PUT', function(response) {
                console.log(response);
                window.location.reload(); // Reload to show the updated image
            });
        } else if (e.target.classList.contains('deleteBtn')) {
            server_request(`/image/${imgId}`, {}, 'DELETE', function(response) {
                // console.log(response);
                // window.location.reload(); // 
                // Change so it immediately deletes instead of reloading
            });
        }
    });
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
