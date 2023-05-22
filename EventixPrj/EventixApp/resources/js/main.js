// Data variables
let startFromSlide = 0;
let slideIndex = startFromSlide;
const slideColors = [
    {
        main: "#ED7CB8",
        background: "#F7CBE6"
    },
    {
        main: "#F0933C",
        background: "#F9D89D"
    },
    {
        main: "#9B69F7",
        background: "#ECD9FC"
    },
    {
        main: "#6BE549",
        background: "#CFF5C9"
    },
    {
        main: "#FEFE53",
        background: "#FAFAC9"
    }
];

// Element variables
let app = document.getElementById("app");
let slides = document.getElementsByClassName("slide");
let coins = [document.getElementsByClassName("coin")[0]];
let findTheTruth = document.getElementById("find-the-truth");

// Summary slide related variables
let startSlide = slides[0];
const amountOfSlides = slides.length;

// Animation for the first slide (begin screen)
if (startFromSlide === 0) startSlide.addEventListener("click", startScreenAnimation, {once : true});
else {
    initiateCoins();
    startSlide.style.marginLeft = ((slideIndex) * -36) + "rem";
}

// When submitting the find the truth component
findTheTruth.addEventListener("submit", (e) => {
    e.preventDefault();

    let button = findTheTruth.getElementsByClassName("btn")[0];
    button.style.translate = "36rem 0";
    findTheTruth.getElementsByClassName("search-glass")[0].style.bottom = "4.5rem";

    for (let i = 0; i < findTheTruth.getElementsByClassName("statements")[0].children.length; i++) findTheTruth.getElementsByClassName("statements")[0].children[i].classList.add("statement--error")
    findTheTruth.getElementsByClassName("statements")[0].children[1].classList.add("statement--check")
});

function startScreenAnimation () {
    startSlide.style.cursor = "initial";
    document.getElementById("begin-bottom").classList.add("title--hide");
    setTimeout(() => {
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
    document.getElementsByClassName("slide__backfigure")[0].classList.add("slide__backfigure--visible");

    // Add all coins to array
    coins[0].style.display = "block";
    for (let i = 0; i < (amountOfSlides - slideIndex - 1); i++) {
        let coin = app.appendChild(coins[0].cloneNode(true));
        coin.style.display = "block";
        coins.push(coin);
    }

    // Calculate the left value so the coins are centered
    let coinsWidth = (amountOfSlides - slideIndex) * 4;
    let leftRemValue = (36 - coinsWidth) / 2 - 0.4;

    setTimeout(() => {
        // Position every coin centered at the bottom of the screen
        for (let i = 0; i < coins.length; i++) {
            setTimeout(() => {
                let coin = coins[i];
                coin.style.top = 67 + "rem";
                coin.style.left = leftRemValue + "rem";
                leftRemValue += 4;
        
                // Let every second coin slide down so they are paired
                if (i % 2) coin.style.top = (parseInt(coin.style.top.slice(0, -3)) + 1.25) + "rem";

                // Give them another CSS transition
                setTimeout(() => coin.style.transition = "left .75s ease-in-out, top 2s ease-in-out", 2000);
            }, 50 * i);
        }
    }, 250);

    // Change slide on click
    app.addEventListener("click", changeSlide);
}

function changeSlide () {
    let slideColor = slideColors[slideIndex];

    coins[slideIndex - startFromSlide].style.left = -100 + "vw";
    startSlide.style.marginLeft = ((slideIndex + 1) * -36) + "rem";
    document.body.style.backgroundColor = slideColor.background;
    document.getElementsByClassName("slide__backfigure")[0].style.backgroundColor = slideColor.main;

    slideIndex++;
    leftRemValue = (36 - (coins.length - slideIndex) * 4) / 2 - 0.4;

    for (let i = slideIndex; i < coins.length; i++) {
        coins[i].style.left = leftRemValue + "rem";
        leftRemValue += 4;
    }
}