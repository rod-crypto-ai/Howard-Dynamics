(() => {
    const body = document.body;
    const nav = document.querySelector("#primary-navigation");
    const navToggle = document.querySelector(".nav-toggle");
    const dropdown = document.querySelector(".nav-dropdown");
    const dropdownTrigger = document.querySelector(".nav-dropdown__trigger");

    if (nav && navToggle) {
        navToggle.addEventListener("click", () => {
            const isOpen = navToggle.getAttribute("aria-expanded") === "true";
            navToggle.setAttribute("aria-expanded", String(!isOpen));
            nav.classList.toggle("is-open", !isOpen);
            body.classList.toggle("nav-open", !isOpen);
        });

        nav.querySelectorAll("a").forEach((link) => {
            link.addEventListener("click", () => {
                navToggle.setAttribute("aria-expanded", "false");
                nav.classList.remove("is-open");
                body.classList.remove("nav-open");
            });
        });
    }

    if (dropdown && dropdownTrigger) {
        dropdownTrigger.addEventListener("click", () => {
            const isOpen = dropdownTrigger.getAttribute("aria-expanded") === "true";
            dropdownTrigger.setAttribute("aria-expanded", String(!isOpen));
            dropdown.classList.toggle("is-open", !isOpen);
        });
    }

    document.addEventListener("click", (event) => {
        if (dropdown && dropdownTrigger && !dropdown.contains(event.target)) {
            dropdown.classList.remove("is-open");
            dropdownTrigger.setAttribute("aria-expanded", "false");
        }
    });

    document.addEventListener("keydown", (event) => {
        if (event.key === "Escape") {
            if (nav && navToggle) {
                nav.classList.remove("is-open");
                navToggle.setAttribute("aria-expanded", "false");
                body.classList.remove("nav-open");
            }
            if (dropdown && dropdownTrigger) {
                dropdown.classList.remove("is-open");
                dropdownTrigger.setAttribute("aria-expanded", "false");
            }
        }
    });

    const revealItems = document.querySelectorAll(".reveal");
    if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add("is-visible");
                        observer.unobserve(entry.target);
                    }
                });
            },
            { threshold: 0.12 }
        );
        revealItems.forEach((item) => observer.observe(item));
    } else {
        revealItems.forEach((item) => item.classList.add("is-visible"));
    }
})();
