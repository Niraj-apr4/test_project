document.addEventListener('DOMContentLoaded', function() {
    // Navigation for the e-card showcase
    const prevButton = document.querySelector('.nav-button.prev');
    const nextButton = document.querySelector('.nav-button.next');
    const showcaseItems = document.querySelectorAll('.showcase-item');
    
    let currentIndex = 0;
    
    // Initially hide all items except the first few
    function updateVisibility() {
        showcaseItems.forEach((item, index) => {
            if (index >= currentIndex && index < currentIndex + 4) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }
    
    prevButton.addEventListener('click', function() {
        if (currentIndex > 0) {
            currentIndex--;
            updateVisibility();
        }
    });
    
    nextButton.addEventListener('click', function() {
        if (currentIndex < showcaseItems.length - 4) {
            currentIndex++;
            updateVisibility();
        }
    });
    
    // Initialize visibility
    updateVisibility();
});
