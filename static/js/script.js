// ============================================
// Student Task Manager
// script.js
// ============================================

// ---------- Auto Hide Flash Messages ----------

setTimeout(function () {

    let alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {

        alert.classList.remove("show");

        alert.classList.add("fade");

        setTimeout(() => {

            alert.remove();

        }, 500);

    });

}, 3000);


// ---------- Search Tasks ----------

const searchInput = document.getElementById("searchInput");

if (searchInput) {

    searchInput.addEventListener("keyup", function () {

        let value = this.value.toLowerCase();

        let rows = document.querySelectorAll("#taskTable tbody tr");

        rows.forEach(function (row) {

            let text = row.innerText.toLowerCase();

            row.style.display = text.includes(value) ? "" : "none";

        });

    });

}


// ---------- Scroll To Top Button ----------

const scrollBtn = document.createElement("button");

scrollBtn.innerHTML = "⬆";

scrollBtn.id = "scrollTopBtn";

scrollBtn.style.position = "fixed";
scrollBtn.style.bottom = "20px";
scrollBtn.style.right = "20px";
scrollBtn.style.display = "none";
scrollBtn.style.padding = "10px 15px";
scrollBtn.style.fontSize = "20px";
scrollBtn.style.border = "none";
scrollBtn.style.borderRadius = "50%";
scrollBtn.style.backgroundColor = "#0d6efd";
scrollBtn.style.color = "white";
scrollBtn.style.cursor = "pointer";
scrollBtn.style.zIndex = "1000";

document.body.appendChild(scrollBtn);

window.addEventListener("scroll", function () {

    if (window.scrollY > 200) {

        scrollBtn.style.display = "block";

    } else {

        scrollBtn.style.display = "none";

    }

});

scrollBtn.addEventListener("click", function () {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

});


// ---------- Live Date & Time ----------

const dateContainer = document.getElementById("currentDateTime");

if (dateContainer) {

    function updateDateTime() {

        const now = new Date();

        dateContainer.innerHTML = now.toLocaleString();

    }

    updateDateTime();

    setInterval(updateDateTime, 1000);

}


// ---------- Welcome Animation ----------

window.addEventListener("load", function () {

    const cards = document.querySelectorAll(".card");

    cards.forEach(function (card, index) {

        card.style.opacity = "0";

        card.style.transform = "translateY(20px)";

        setTimeout(function () {

            card.style.transition = "0.5s";

            card.style.opacity = "1";

            card.style.transform = "translateY(0)";

        }, index * 150);

    });

});


// ---------- Confirm Before Logout ----------

const logoutLink = document.querySelector('a[href="/logout"]');

if (logoutLink) {

    logoutLink.addEventListener("click", function (e) {

        if (!confirm("Are you sure you want to logout?")) {

            e.preventDefault();

        }

    });

}


// ---------- Dashboard Counter Animation ----------

const numbers = document.querySelectorAll(".card h2");

numbers.forEach(function (number) {

    const target = parseInt(number.innerText);

    if (!isNaN(target)) {

        let count = 0;

        const increment = Math.max(1, Math.ceil(target / 30));

        const timer = setInterval(function () {

            count += increment;

            if (count >= target) {

                count = target;

                clearInterval(timer);

            }

            number.innerText = count;

        }, 30);

    }

});


// ---------- Footer Year ----------

const footerYear = document.getElementById("year");

if (footerYear) {

    footerYear.innerHTML = new Date().getFullYear();

}