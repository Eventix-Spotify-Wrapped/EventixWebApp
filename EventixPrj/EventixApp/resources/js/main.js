// Variables
const amountOfSlide = 7;
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
let app = document.getElementById("app");
let slides = document.getElementsByClassName("slide");
let coins = [document.getElementsByClassName("coin")[0]];

// Add all coins to array
for (let i = 0; i < (amountOfSlide - 1); i++) coins.push( app.appendChild(coins[0].cloneNode(true)));

// When the slot machine-handle is clicked
document.getElementById("machine").addEventListener("click", () => {

    // Pull the lever downwards with a CSS class
    document.getElementsByClassName("lever")[0].classList.add("lever--active");

    // Animate the bottom slide
    document.getElementsByClassName("slide__backfigure")[0].classList.add("slide__backfigure--visible");

    // Calculate the left value so the coins are centered
    let coinsWidth = amountOfSlide * 4;
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

    setTimeout(() => {
        let slideIndex = 0;

        app.addEventListener("click", () => {
            let slideColor = slideColors[slideIndex];

            coins[slideIndex].style.left = -100 + "vw";
            slides[0].style.marginLeft = ((slideIndex + 1) * -36) + "rem";
            document.getElementsByClassName("slide__wrapper")[0].style.backgroundColor = slideColor.background;
            document.getElementsByClassName("slide__backfigure")[0].style.backgroundColor = slideColor.main;

            slideIndex++;

            coinsWidth = (coins.length - slideIndex) * 4;
            leftRemValue = (36 - coinsWidth) / 2 - 0.4;

            for (let i = slideIndex; i < coins.length; i++) {
                let coin = coins[i];
                coin.style.left = leftRemValue + "rem";
                leftRemValue += 4;
            }
        });
    }, 1);
}, {once : true});