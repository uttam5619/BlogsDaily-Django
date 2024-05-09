const accordionItems = document.querySelectorAll('.accordion-item');

// Add click event listener to each accordion header
accordionItems.forEach(item => {
    const header = item.querySelector('.accordion-header');
    header.addEventListener('click', () => {
        // Toggle active class to expand/collapse accordion content
        item.classList.toggle('active');
    });
});