// Counup npm library for the countup animation
import { CountUp } from 'countup.js';

// Get slideColors from the JSON
fetch('/static/js/slideColors.json').then(
    (response) => response.json()
).then(
    (json) => main(json)
);

async function main (slideColors) {
    // Data variables
    let startFromSlide = 0;
    const coinNavigation = true;
    let slideIndex = startFromSlide;

    // Element variables
    let app = document.getElementById("app");
    let slides = document.getElementsByClassName("slide");
    let coins = [document.getElementsByClassName("coin")[0]];
    let findTheTruth = document.getElementById("find-the-truth-form");

    // Summary slide related variables
    let colorIndex = 0;
    let startSlide = slides[0];
    const amountOfSlides = slides.length;

    // Calculate the left value so the coins are centered when placed
    let coinsWidth = (amountOfSlides - slideIndex - 1) * 4;
    let coinLeftRemValue = (36 - coinsWidth) / 2 - 0.4;

    // Determine from which slide to start and start the summary accordingly
    if (startFromSlide === 0) startSlide.addEventListener("click", startScreenAnimation, {once : true});
    else {
        initiateCoins();
        if (!coinNavigation) startSlide.style.transition = "none";
        startSlide.style.marginLeft = slideIndex * -36 + "rem";
    }

    // When submitting the find the truth component
    findTheTruth.addEventListener("submit", (e) => {
        // Stop the regular submitting of the form
        e.preventDefault();

        // Variables
        let button = findTheTruth.getElementsByClassName("btn")[0];
        let statements = findTheTruth.getElementsByClassName("statements")[0].children;

        // Hide the button after submuitting
        button.style.translate = "36rem 0";

        // Show the searchglass illustation
        findTheTruth.getElementsByClassName("search-glass")[0].style.bottom = "4.5rem";

        // Give error classes to all statements
        for (let i = 0; i < statements.length; i++) statements[i].classList.add("statement--error")

        // Give the right statement the right class (hardcoded for now)
        statements[0].classList.add("statement--check");

        // Eventlistener to show the slide with validation of the statemnt
        document.getElementById("find-the-truth").addEventListener("click", () => {

            // Hide all answers that are not the right one or clarification
            for (let i = 0; i < statements.length; i++) if (!statements[i].classList.contains("statement--check")) statements[i].style.display = "none";
            
            // Hide the search glass illustration
            findTheTruth.getElementsByClassName("search-glass")[0].style.bottom = "-20rem";

            // Show the correctionbox with the celebratory illustration
            setTimeout(() => {
                findTheTruth.getElementsByClassName("correction-box")[0].classList.add("correction-box--active")
                findTheTruth.getElementsByClassName("celebrate")[0].classList.add("celebrate--active")
            }, 500);

            // Go the next slide when clicking on the current slide
            setTimeout(() => document.getElementById("find-the-truth").addEventListener("click", changeSlide), 1000);
        });
    });

    function startScreenAnimation () {
        // Hide clickabe cursor
        startSlide.style.cursor = "initial";

        // Hide the text before starting the plug animation
        document.getElementById("begin-bottom").classList.add("title--hide");

        setTimeout(() => {
            // Start the plug animation
            document.getElementById("plug").classList.add("active");
            setTimeout(() => document.getElementsByClassName("begin-illustration")[0].classList.add("begin-illustration--start"), 1000);

            setTimeout(() => {
                // Pull the lever downwards with a CSS class
                document.getElementsByClassName("lever")[0].classList.add("lever--active");

                // Animate coins and bottom slide
                initiateCoins();
            }, 2750);
        }, 750);
    }

    function initiateCoins () {
        // Animate bottom slide
        if (coinNavigation) document.getElementById("slide-backfigure").classList.add("slide__backfigure--visible");

        // Add all coins to array
        if (coinNavigation) {
            coins[0].style.display = "block";
            for (let i = 0; i < (amountOfSlides - slideIndex - 2); i++) {
                let coin = app.appendChild(coins[0].cloneNode(true));
                coin.style.display = "block";
                coins.push(coin);
            }
        }

        setTimeout(() => {
            // Position every coin centered at the bottom of the screen
            for (let i = 0; i < coins.length; i++) {
                setTimeout(() => {
                    let coin = coins[i];
                    coin.style.top = 67 + "rem";
                    coin.style.left = coinLeftRemValue + "rem";
                    coinLeftRemValue += 4;
            
                    // Let every second coin slide down so they are paired
                    if (i % 2) coin.style.top = (parseInt(coin.style.top.slice(0, -3)) + 1.25) + "rem";

                    // Give the coins a different CSS transition (time)
                    setTimeout(() => coin.style.transition = "left .75s ease-in-out, top 2s ease-in-out", 2000);
                }, 50 * i);
            }

            // Change slide on click
            for (let i = 0; i < slides.length; i++) if (slides[i].id != "find-the-truth") slides[i].addEventListener("click", changeSlide);
        }, 250);
    }

    function changeSlide () {
        // Next color
        colorIndex++;

        // Get new slideColors
        if (colorIndex >= slideColors.length) colorIndex = 0;
        let slideColor = slideColors[colorIndex];

        // Hide the coin that represents the next slide
        if (coins[slideIndex - startFromSlide]) coins[slideIndex - startFromSlide].style.left = -64 + "rem";

        // Change the background and front colors of each slide
        document.body.style.backgroundColor = slideColor.background;
        document.getElementById("slide-backfigure").style.backgroundColor = slideColor.main;

        // Up the variable so it represents the next slide
        slideIndex++;

        // Show the next slide using a negative margin
        startSlide.style.marginLeft = (slideIndex * -36) + "rem";

        switch (slides[slideIndex].id) {
            case "average-age-visitors":
                setTimeout(() => document.getElementsByClassName("visitor-cards")[0].classList.add("visitor-cards--show"), 1600);
            break;

            case "date-most-ticket-sales":
                setTimeout(() => {
                    // Start the calander animation
                    document.getElementById("calander-illustration").classList.add("calander--normal");
                    setTimeout(() => document.getElementsByClassName("date")[0].classList.add("date--show"), 1000);
                }, 1600);
            break;

            case "ticket-sale-percentage":
                // Initiate the countup animation on the ticket percentage slide
                new CountUp(document.getElementById("ticketPercentageCountUp"), 95, { duration: 3 }).start();
            break;

            case "visitor-origins":
                // Initiate the countup animation on the visitor origins page
                new CountUp(document.getElementById("visitorOriginsPercentageCountUp"), 95, { duration: 3 }).start();
            break;

            case "end-overview":
                // Hide logo on share screen
                document.getElementsByClassName("logo")[0].style.display = "none";

                // Remove the coins and backslide on the last screen for the final overview
                document.getElementById("slide-backfigure").classList.remove("slide__backfigure--visible");
                coins[coins.length - 1].style.top = 80 + "rem";
            break;
        }

        // Center the coins at the bottom of the slide again after the width is adjusted (one coin dissapeared)
        centerCoins();
    }

    function centerCoins () {
        coinLeftRemValue = (36 - (coins.length - slideIndex) * 4) / 2 - 0.4;
        for (let i = slideIndex; i < coins.length; i++) {
            coins[i].style.left = coinLeftRemValue + "rem";
            coinLeftRemValue += 4;
        }
    }
}