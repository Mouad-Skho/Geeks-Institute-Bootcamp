var activeCategory = "All";

function filterObjects(c) {
    activeCategory = c;
    applyFilters();
}
function myFunction() {
    applyFilters();
  }

function applyFilters() {
    var input, filter, card, i, txtValue, matchesText, matchesCategory, visibleCount = 0;
    input = document.getElementById('myInput');
    filter = input.value.toUpperCase();
    card = document.getElementsByClassName("card");
    for (i = 0; i < card.length; i++) {
        removeClass(card[i], "show");
        txtValue = card[i].dataset.title || card[i].textContent;
        matchesText = txtValue.toUpperCase().indexOf(filter) > -1;
        matchesCategory = activeCategory == "All" || card[i].dataset.category == activeCategory;
        if (matchesText && matchesCategory) {
            addClass(card[i], "show");
            visibleCount++;
        }
    }
    emptyState(visibleCount);
    updateBookCount();
}
function addClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {
            element.className += " " + arr2[i];
        }
    }
}
function removeClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}
let btnContainer = document.getElementById("button");
let btns = btnContainer.getElementsByClassName("btn");
for (let i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {

        let current = document.getElementsByClassName("active");
        filterObjects(this.id);
        if (current.length > 0) {
            current[0].className =
                current[0].className.replace(" active", "");
        }

        this.className += " active";
    });
}
const cardGrid = document.getElementById("cards-grid");

catalogItems.forEach(item => {
    const card = document.createElement("article");
    card.classList.add("card");
    card.dataset.category = item.category;
        card.dataset.title = item.title;
        card.dataset.id = item.id;
    card.innerHTML = `
        <img class="card-image" src="${item.image}" alt="${item.title}">
        <div class="card-content">
            <h2><span class="title">${item.title}</span><span class="category">${item.category}</span></h2>
            <p class="card-info">${item.metric}</p>
            <p>${item.shortDescription}</p>
            <button class="btn-link" id="${item.id}">Read More →</button>
        </div>
    `;
    cardGrid.appendChild(card);
});

filterObjects("All");

var originalOrder = [...cardGrid.getElementsByClassName("card")];

function sortCards(mode) {
    var cards;
    if (mode === "default") {
        cards = originalOrder;
    } else {
        cards = [...cardGrid.getElementsByClassName("card")].sort(function (a, b) {
            var byTitle = a.dataset.title.localeCompare(b.dataset.title);
            return mode === "za" ? -byTitle : byTitle;
        });
    }
    cards.forEach(function (card) {
        cardGrid.appendChild(card);
    });
}

var dropdown = document.querySelector(".dropdown");
var dropbtn = document.querySelector(".dropbtn");
var dropdownContent = document.querySelector(".dropdown-content");

dropbtn.addEventListener("click", function (event) {
    event.stopPropagation();
    dropdown.classList.toggle("open");
});

dropdownContent.addEventListener("click", function () {
    dropdown.classList.remove("open");
});

document.addEventListener("click", function (event) {
    if (!dropdown.contains(event.target)) {
        dropdown.classList.remove("open");
    }
});

function syncThemeToggle(isDark) {
    var toggle = document.querySelector(".theme-toggle");
    toggle.setAttribute("aria-checked", isDark ? "false" : "true");
    toggle.setAttribute("aria-label", isDark ? "Switch to light mode" : "Switch to dark mode");
}

function toggleDarkMode() {
    var isDark = document.body.classList.toggle("dark-mode");
    syncThemeToggle(isDark);
    localStorage.setItem("theme", isDark ? "dark" : "light");
}

document.querySelector(".theme-toggle").addEventListener("click", toggleDarkMode);

var startDark = localStorage.getItem("theme") === "dark";
document.body.classList.toggle("dark-mode", startDark);
syncThemeToggle(startDark);

function emptyState(visibleCount) {
    const emptyStateContainer = document.getElementById("empty-state");
    if (visibleCount === 0) {
        emptyStateContainer.classList.remove("hide");
    } else {
        emptyStateContainer.classList.add("hide");
    }
}
function updateBookCount() {
    const visibleCards = document.getElementsByClassName("card show");
    const count = visibleCards.length;
    document.getElementById("book-count").textContent =
        count + (count === 1 ? " amazing book" : " amazing books");
}
function openDetails(item) {
    const details = catalogItems.find(book => book.id === Number(item));
    if (!details) return;
    document.getElementById("modal-body").innerHTML = `
        <img class="card-image-modal card-image"  src="${details.image}" alt="${details.title}">
        <div class="card-content">
            <h2>${details.title}</h2>
            <p class="category">${details.category}</p>
            <p class="card-info">${details.metric}</p>
            <p>${details.fullDetails}</p>
        </div>
    `;
}
// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var card = document.getElementsByClassName("card");
for (var i = 0; i < card.length; i++) {
    card[i].onclick = function() {
        modal.style.display = "block";
        openDetails(this.dataset.id);
    }
}
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  
}