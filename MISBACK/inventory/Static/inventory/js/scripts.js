// backend/inventory/static/inventory/js/scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Function to confirm deletion of an inventory item
    function confirmDeletion(event) {
        const confirmed = confirm("Are you sure you want to delete this item?");
        if (!confirmed) {
            event.preventDefault();
        }
    }

    // Add event listeners to delete buttons
    const deleteButtons = document.querySelectorAll('.delete-button');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', confirmDeletion);
    });

    // AJAX request to load inventory items
    function loadInventoryItems() {
        fetch('/inventory/')
            .then(response => response.json())
            .then(data => {
                const inventoryList = document.querySelector('.inventory-list');
                inventoryList.innerHTML = '';
                data.forEach(item => {
                    const listItem = document.createElement('li');
                    listItem.innerHTML = `
                        <a href="/inventory/${item.id}/">${item.name}</a> (Quantity: ${item.quantity})
                        <a href="/inventory/${item.id}/edit/" class="edit-button">Edit</a>
                        <a href="/inventory/${item.id}/delete/" class="delete-button">Delete</a>
                    `;
                    inventoryList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error loading inventory items:', error));
    }

    // Load inventory items on page load
    loadInventoryItems();
});
