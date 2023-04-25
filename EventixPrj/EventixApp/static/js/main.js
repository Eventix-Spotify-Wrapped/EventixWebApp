/******/ (() => { // webpackBootstrap
/******/ 	var __webpack_modules__ = ({

/***/ "./EventixPrj/EventixApp/resources/js/main.js":
/*!****************************************************!*\
  !*** ./EventixPrj/EventixApp/resources/js/main.js ***!
  \****************************************************/
/***/ (() => {

// Variables
var amountOfSlide = 7;
var slideColors = [{
  main: "#ED7CB8",
  background: "#F7CBE6"
}, {
  main: "#F0933C",
  background: "#F9D89D"
}, {
  main: "#9B69F7",
  background: "#ECD9FC"
}, {
  main: "#6BE549",
  background: "#CFF5C9"
}, {
  main: "#FEFE53",
  background: "#FAFAC9"
}];
var app = document.getElementById("app");
var slides = document.getElementsByClassName("slide");
var coins = [document.getElementsByClassName("coin")[0]];

// Add all coins to array
for (var i = 0; i < amountOfSlide - 1; i++) coins.push(app.appendChild(coins[0].cloneNode(true)));

// When the slot machine-handle is clicked
document.getElementById("machine").addEventListener("click", function () {
  // Pull the lever downwards with a CSS class
  document.getElementsByClassName("lever")[0].classList.add("lever--active");

  // Animate the bottom slide
  document.getElementsByClassName("slide__backfigure")[0].classList.add("slide__backfigure--visible");

  // Calculate the left value so the coins are centered
  var coinsWidth = amountOfSlide * 4;
  var leftRemValue = (36 - coinsWidth) / 2 - 0.4;
  setTimeout(function () {
    var _loop = function _loop(_i) {
      setTimeout(function () {
        var coin = coins[_i];
        coin.style.top = 67 + "rem";
        coin.style.left = leftRemValue + "rem";
        leftRemValue += 4;

        // Let every second coin slide down so they are paired
        if (_i % 2) coin.style.top = parseInt(coin.style.top.slice(0, -3)) + 1.25 + "rem";

        // Give them another CSS transition
        setTimeout(function () {
          return coin.style.transition = "left .75s ease-in-out, top 2s ease-in-out";
        }, 2000);
      }, 50 * _i);
    };
    // Position every coin centered at the bottom of the screen
    for (var _i = 0; _i < coins.length; _i++) {
      _loop(_i);
    }
  }, 250);
  setTimeout(function () {
    var slideIndex = 0;
    app.addEventListener("click", function () {
      var slideColor = slideColors[slideIndex];
      coins[slideIndex].style.left = -100 + "vw";
      slides[0].style.marginLeft = (slideIndex + 1) * -36 + "rem";
      document.getElementsByClassName("slide__wrapper")[0].style.backgroundColor = slideColor.background;
      document.getElementsByClassName("slide__backfigure")[0].style.backgroundColor = slideColor.main;
      slideIndex++;
      coinsWidth = (coins.length - slideIndex) * 4;
      leftRemValue = (36 - coinsWidth) / 2 - 0.4;
      for (var _i2 = slideIndex; _i2 < coins.length; _i2++) {
        var coin = coins[_i2];
        coin.style.left = leftRemValue + "rem";
        leftRemValue += 4;
      }
    });
  }, 1);
}, {
  once: true
});

/***/ }),

/***/ "./EventixPrj/EventixApp/resources/sass/stylesheet.sass":
/*!**************************************************************!*\
  !*** ./EventixPrj/EventixApp/resources/sass/stylesheet.sass ***!
  \**************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

"use strict";
__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId](module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = __webpack_modules__;
/******/ 	
/************************************************************************/
/******/ 	/* webpack/runtime/chunk loaded */
/******/ 	(() => {
/******/ 		var deferred = [];
/******/ 		__webpack_require__.O = (result, chunkIds, fn, priority) => {
/******/ 			if(chunkIds) {
/******/ 				priority = priority || 0;
/******/ 				for(var i = deferred.length; i > 0 && deferred[i - 1][2] > priority; i--) deferred[i] = deferred[i - 1];
/******/ 				deferred[i] = [chunkIds, fn, priority];
/******/ 				return;
/******/ 			}
/******/ 			var notFulfilled = Infinity;
/******/ 			for (var i = 0; i < deferred.length; i++) {
/******/ 				var [chunkIds, fn, priority] = deferred[i];
/******/ 				var fulfilled = true;
/******/ 				for (var j = 0; j < chunkIds.length; j++) {
/******/ 					if ((priority & 1 === 0 || notFulfilled >= priority) && Object.keys(__webpack_require__.O).every((key) => (__webpack_require__.O[key](chunkIds[j])))) {
/******/ 						chunkIds.splice(j--, 1);
/******/ 					} else {
/******/ 						fulfilled = false;
/******/ 						if(priority < notFulfilled) notFulfilled = priority;
/******/ 					}
/******/ 				}
/******/ 				if(fulfilled) {
/******/ 					deferred.splice(i--, 1)
/******/ 					var r = fn();
/******/ 					if (r !== undefined) result = r;
/******/ 				}
/******/ 			}
/******/ 			return result;
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/hasOwnProperty shorthand */
/******/ 	(() => {
/******/ 		__webpack_require__.o = (obj, prop) => (Object.prototype.hasOwnProperty.call(obj, prop))
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/make namespace object */
/******/ 	(() => {
/******/ 		// define __esModule on exports
/******/ 		__webpack_require__.r = (exports) => {
/******/ 			if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 				Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 			}
/******/ 			Object.defineProperty(exports, '__esModule', { value: true });
/******/ 		};
/******/ 	})();
/******/ 	
/******/ 	/* webpack/runtime/jsonp chunk loading */
/******/ 	(() => {
/******/ 		// no baseURI
/******/ 		
/******/ 		// object to store loaded and loading chunks
/******/ 		// undefined = chunk not loaded, null = chunk preloaded/prefetched
/******/ 		// [resolve, reject, Promise] = chunk loading, 0 = chunk loaded
/******/ 		var installedChunks = {
/******/ 			"/EventixPrj/EventixApp/static/js/main": 0,
/******/ 			"EventixPrj/EventixApp/static/css/stylesheet": 0
/******/ 		};
/******/ 		
/******/ 		// no chunk on demand loading
/******/ 		
/******/ 		// no prefetching
/******/ 		
/******/ 		// no preloaded
/******/ 		
/******/ 		// no HMR
/******/ 		
/******/ 		// no HMR manifest
/******/ 		
/******/ 		__webpack_require__.O.j = (chunkId) => (installedChunks[chunkId] === 0);
/******/ 		
/******/ 		// install a JSONP callback for chunk loading
/******/ 		var webpackJsonpCallback = (parentChunkLoadingFunction, data) => {
/******/ 			var [chunkIds, moreModules, runtime] = data;
/******/ 			// add "moreModules" to the modules object,
/******/ 			// then flag all "chunkIds" as loaded and fire callback
/******/ 			var moduleId, chunkId, i = 0;
/******/ 			if(chunkIds.some((id) => (installedChunks[id] !== 0))) {
/******/ 				for(moduleId in moreModules) {
/******/ 					if(__webpack_require__.o(moreModules, moduleId)) {
/******/ 						__webpack_require__.m[moduleId] = moreModules[moduleId];
/******/ 					}
/******/ 				}
/******/ 				if(runtime) var result = runtime(__webpack_require__);
/******/ 			}
/******/ 			if(parentChunkLoadingFunction) parentChunkLoadingFunction(data);
/******/ 			for(;i < chunkIds.length; i++) {
/******/ 				chunkId = chunkIds[i];
/******/ 				if(__webpack_require__.o(installedChunks, chunkId) && installedChunks[chunkId]) {
/******/ 					installedChunks[chunkId][0]();
/******/ 				}
/******/ 				installedChunks[chunkId] = 0;
/******/ 			}
/******/ 			return __webpack_require__.O(result);
/******/ 		}
/******/ 		
/******/ 		var chunkLoadingGlobal = self["webpackChunkeventixwebapp"] = self["webpackChunkeventixwebapp"] || [];
/******/ 		chunkLoadingGlobal.forEach(webpackJsonpCallback.bind(null, 0));
/******/ 		chunkLoadingGlobal.push = webpackJsonpCallback.bind(null, chunkLoadingGlobal.push.bind(chunkLoadingGlobal));
/******/ 	})();
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module depends on other loaded chunks and execution need to be delayed
/******/ 	__webpack_require__.O(undefined, ["EventixPrj/EventixApp/static/css/stylesheet"], () => (__webpack_require__("./EventixPrj/EventixApp/resources/js/main.js")))
/******/ 	var __webpack_exports__ = __webpack_require__.O(undefined, ["EventixPrj/EventixApp/static/css/stylesheet"], () => (__webpack_require__("./EventixPrj/EventixApp/resources/sass/stylesheet.sass")))
/******/ 	__webpack_exports__ = __webpack_require__.O(__webpack_exports__);
/******/ 	
/******/ })()
;