/**
 * Homepath Alliance - Global JavaScript
 * Production-ready JavaScript for nonprofit housing website
 */

// ======================
// Initialization
// ======================
$(document).ready(function() {
    initGlobalScripts();
});

function initGlobalScripts() {
    // Initialize all global behaviors
    initAjaxContentLoading();
    initAjaxForms();
    initScrollEffects();
    initSmoothScroll();
    initMobileMenu();
    initDarkModeToggle();
    initEventDelegation();
    ensureWhiteText();
}

// ======================
// AJAX Content Loading
// ======================
function initAjaxContentLoading() {
    // Generic AJAX function for dynamic content loading
    window.loadContentViaAjax = function(url, targetContainer) {
        const $target = $(targetContainer);
        const $loadingIndicator = $('<div class="loading-message">Loading content...</div>');
        
        // Show loading indicator
        $target.html($loadingIndicator);
        $target.attr('aria-busy', 'true');
        
        $.ajax({
            url: url,
            type: 'GET',
            dataType: 'html',
            success: function(data) {
                $target.html(data);
                $target.attr('aria-busy', 'false');
                // Update ARIA attributes and focus for accessibility
                updateAriaForAjaxContent($target);
                focusFirstFocusableElement($target);
                console.log('Content loaded successfully from ' + url);
            },
            error: function(xhr, status, error) {
                $target.html('<div class="error-message">Failed to load content. Please try again later.</div>');
                $target.attr('aria-busy', 'false');
                console.error('AJAX content loading failed:', error);
            }
        });
    };
    
    // Example usage for dynamic content loading
    // loadContentViaAjax('/api/articles/', '#dynamic-content');
}

// ======================
// Global Form Handling via AJAX
// ======================
function initAjaxForms() {
    $(document).on('submit', '.ajax-form', function(e) {
        e.preventDefault();
        
        const $form = $(this);
        const $feedback = $form.find('.form-feedback');
        const formData = $form.serialize();
        const formAction = $form.attr('action') || window.location.href;
        const formMethod = $form.attr('method') || 'POST';
        
        // Clear previous feedback
        $feedback.empty();
        
        $.ajax({
            url: formAction,
            type: formMethod,
            data: formData,
            dataType: 'json',
            beforeSend: function() {
                // Disable submit button during submission
                $form.find('[type="submit"]').prop('disabled', true);
            },
            success: function(response) {
                $feedback.html('<div class="success-message">Form submitted successfully!</div>');
                $form[0].reset(); // Reset form on success
                console.log('Form submitted successfully', response);

            },
            error: function(xhr, status, error) {
                $feedback.html('<div class="error-message">Error submitting form. Please try again.</div>');
                console.error('Form submission failed:', error);
            },
            complete: function() {
                // Re-enable submit button
                $form.find('[type="submit"]').prop('disabled', false);
            }
        });
    });
}

// ======================
// Animations & Scroll Effects
// ======================
function initScrollEffects() {
    // Check if user prefers reduced motion
    const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    
    if (prefersReducedMotion) {
        // Apply simpler animations for users who prefer reduced motion
        $('.fade-in-on-scroll').addClass('visible');
        $('.slide-in-on-scroll').addClass('visible');
        return;
    }
    
    // Animation function for elements entering viewport
    function animateElementsOnScroll() {
        $('.fade-in-on-scroll:not(.animated)').each(function() {
            const elementTop = $(this).offset().top;
            const elementHeight = $(this).outerHeight();
            const windowHeight = $(window).height();
            const scrollTop = $(window).scrollTop();
            
            // Trigger animation when element is 75% in view
            if (elementTop < (scrollTop + windowHeight - elementHeight * 0.25)) {
                $(this).addClass('animated').animate({opacity: 1}, 600);
            }
        });
        
        $('.slide-in-on-scroll:not(.animated)').each(function() {
            const elementTop = $(this).offset().top;
            const elementHeight = $(this).outerHeight();
            const windowHeight = $(window).height();
            const scrollTop = $(window).scrollTop();
            
            // Trigger animation when element is 75% in view
            if (elementTop < (scrollTop + windowHeight - elementHeight * 0.25)) {
                $(this).addClass('animated').css({
                    transform: 'translateX(0)',
                    opacity: 1
                });
            }
        });
    }
    
    // Initial check on page load
    animateElementsOnScroll();
    
    // Check on scroll
    $(window).on('scroll', function() {
        animateElementsOnScroll();
    });
}

// ======================
// Smooth Scroll
// ======================
function initSmoothScroll() {
    $('a[href^="#"]').on('click', function(e) {
        e.preventDefault();
        
        const target = $($(this).attr('href'));
        if (target.length) {
            $('html, body').animate({
                scrollTop: target.offset().top
            }, 600, 'swing');
        }
    });
}

// ======================
// Mobile Menu Toggle & UI Utilities
// ======================
function initMobileMenu() {
    $('.menu-toggle').on('click', function() {
        const $button = $(this);
        const $menu = $('.mobile-menu');
        const isOpen = $menu.hasClass('is-open');
        
        if (isOpen) {
            $menu.removeClass('is-open').slideUp(300);
            $button.attr('aria-expanded', 'false');
        } else {
            $menu.addClass('is-open').slideDown(300);
            $button.attr('aria-expanded', 'true');
        }
    });
}

function initDarkModeToggle() {
    // Check for saved theme preference or respect OS setting
    const savedTheme = localStorage.getItem('theme');
    const osPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    if (savedTheme === 'dark' || (!savedTheme && osPrefersDark)) {
        $('body').addClass('theme-dark');
    }
    
    $('.theme-toggle').on('click', function() {
        $('body').toggleClass('theme-dark');
        const isDark = $('body').hasClass('theme-dark');
        localStorage.setItem('theme', isDark ? 'dark' : 'light');
        // Ensure white text is applied when theme changes
        ensureWhiteText();
    });
}

// ======================
// Event Delegation & Dynamic Content
// ======================
function initEventDelegation() {
    // Handle clicks on dynamically added buttons
    $(document).on('click', '.dynamic-button', function() {
        // Example handler for dynamically added elements
        console.log('Dynamic button clicked');
    });
    
    // Handle form submissions for dynamically added forms
    $(document).on('submit', '.dynamic-ajax-form', function(e) {
        e.preventDefault();
        console.log('Dynamic AJAX form submitted');
        // Process dynamic form here
    });
}

// ======================
// Accessibility Helpers
// ======================
function updateAriaForAjaxContent($container) {
    // Update ARIA attributes for AJAX loaded content
    $container.find('[role="alert"]').each(function() {
        // Ensure alerts are announced to screen readers
        const $alert = $(this);
        if (!$alert.attr('aria-live')) {
            $alert.attr('aria-live', 'polite');
        }
    });
    console.log('Updated ARIA attributes for AJAX content');
}

function focusFirstFocusableElement($container) {
    // Focus the first focusable element in the container for accessibility
    const $firstFocusable = $container.find(':focusable').first();
    if ($firstFocusable.length) {
        $firstFocusable.focus();
    }
}

// ======================
// Text Color Utilities
// ======================
function ensureWhiteText() {
    // Ensure all text elements have white color in dark mode
    if ($('body').hasClass('theme-dark') || window.matchMedia('(prefers-color-scheme: dark)').matches) {
        $('.force-white-text, .text-white-override').addClass('text-white');
    }
}