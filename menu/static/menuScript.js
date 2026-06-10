document.addEventListener("DOMContentLoaded", function () {

    const searchInput = document.getElementById("searchInput");
    const searchBtn = document.getElementById("searchBtn");
    const noResults = document.getElementById("noResults");

    const menuItems = document.querySelectorAll(".menu-item");

    if (!searchInput || !searchBtn || !noResults) return;

    function filterMenu() {

        const query = searchInput.value.trim().toLowerCase();

        let anyVisible = false;

        menuItems.forEach(item => {

            const nameEl = item.querySelector("h4");

            if (!nameEl) return;

            const name = nameEl.textContent.toLowerCase();

            if (name.includes(query)) {
                item.style.display = "flex";
                anyVisible = true;
            } else {
                item.style.display = "none";
            }
        });

        noResults.style.display = anyVisible ? "none" : "block";
    }

    // click search
    searchBtn.addEventListener("click", filterMenu);

    // live search
    searchInput.addEventListener("input", filterMenu);

    // ENTER key support 🔥
    searchInput.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
            filterMenu();
        }
    });

});