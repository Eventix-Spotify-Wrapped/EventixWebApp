/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ "./EventixPrj/EventixApp/resources/js/main.js":
/*!****************************************************!*\
  !*** ./EventixPrj/EventixApp/resources/js/main.js ***!
  \****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony import */ var countup_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! countup.js */ "./node_modules/countup.js/dist/countUp.min.js");
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _regeneratorRuntime() { "use strict"; /*! regenerator-runtime -- Copyright (c) 2014-present, Facebook, Inc. -- license (MIT): https://github.com/facebook/regenerator/blob/main/LICENSE */ _regeneratorRuntime = function _regeneratorRuntime() { return exports; }; var exports = {}, Op = Object.prototype, hasOwn = Op.hasOwnProperty, defineProperty = Object.defineProperty || function (obj, key, desc) { obj[key] = desc.value; }, $Symbol = "function" == typeof Symbol ? Symbol : {}, iteratorSymbol = $Symbol.iterator || "@@iterator", asyncIteratorSymbol = $Symbol.asyncIterator || "@@asyncIterator", toStringTagSymbol = $Symbol.toStringTag || "@@toStringTag"; function define(obj, key, value) { return Object.defineProperty(obj, key, { value: value, enumerable: !0, configurable: !0, writable: !0 }), obj[key]; } try { define({}, ""); } catch (err) { define = function define(obj, key, value) { return obj[key] = value; }; } function wrap(innerFn, outerFn, self, tryLocsList) { var protoGenerator = outerFn && outerFn.prototype instanceof Generator ? outerFn : Generator, generator = Object.create(protoGenerator.prototype), context = new Context(tryLocsList || []); return defineProperty(generator, "_invoke", { value: makeInvokeMethod(innerFn, self, context) }), generator; } function tryCatch(fn, obj, arg) { try { return { type: "normal", arg: fn.call(obj, arg) }; } catch (err) { return { type: "throw", arg: err }; } } exports.wrap = wrap; var ContinueSentinel = {}; function Generator() {} function GeneratorFunction() {} function GeneratorFunctionPrototype() {} var IteratorPrototype = {}; define(IteratorPrototype, iteratorSymbol, function () { return this; }); var getProto = Object.getPrototypeOf, NativeIteratorPrototype = getProto && getProto(getProto(values([]))); NativeIteratorPrototype && NativeIteratorPrototype !== Op && hasOwn.call(NativeIteratorPrototype, iteratorSymbol) && (IteratorPrototype = NativeIteratorPrototype); var Gp = GeneratorFunctionPrototype.prototype = Generator.prototype = Object.create(IteratorPrototype); function defineIteratorMethods(prototype) { ["next", "throw", "return"].forEach(function (method) { define(prototype, method, function (arg) { return this._invoke(method, arg); }); }); } function AsyncIterator(generator, PromiseImpl) { function invoke(method, arg, resolve, reject) { var record = tryCatch(generator[method], generator, arg); if ("throw" !== record.type) { var result = record.arg, value = result.value; return value && "object" == _typeof(value) && hasOwn.call(value, "__await") ? PromiseImpl.resolve(value.__await).then(function (value) { invoke("next", value, resolve, reject); }, function (err) { invoke("throw", err, resolve, reject); }) : PromiseImpl.resolve(value).then(function (unwrapped) { result.value = unwrapped, resolve(result); }, function (error) { return invoke("throw", error, resolve, reject); }); } reject(record.arg); } var previousPromise; defineProperty(this, "_invoke", { value: function value(method, arg) { function callInvokeWithMethodAndArg() { return new PromiseImpl(function (resolve, reject) { invoke(method, arg, resolve, reject); }); } return previousPromise = previousPromise ? previousPromise.then(callInvokeWithMethodAndArg, callInvokeWithMethodAndArg) : callInvokeWithMethodAndArg(); } }); } function makeInvokeMethod(innerFn, self, context) { var state = "suspendedStart"; return function (method, arg) { if ("executing" === state) throw new Error("Generator is already running"); if ("completed" === state) { if ("throw" === method) throw arg; return doneResult(); } for (context.method = method, context.arg = arg;;) { var delegate = context.delegate; if (delegate) { var delegateResult = maybeInvokeDelegate(delegate, context); if (delegateResult) { if (delegateResult === ContinueSentinel) continue; return delegateResult; } } if ("next" === context.method) context.sent = context._sent = context.arg;else if ("throw" === context.method) { if ("suspendedStart" === state) throw state = "completed", context.arg; context.dispatchException(context.arg); } else "return" === context.method && context.abrupt("return", context.arg); state = "executing"; var record = tryCatch(innerFn, self, context); if ("normal" === record.type) { if (state = context.done ? "completed" : "suspendedYield", record.arg === ContinueSentinel) continue; return { value: record.arg, done: context.done }; } "throw" === record.type && (state = "completed", context.method = "throw", context.arg = record.arg); } }; } function maybeInvokeDelegate(delegate, context) { var methodName = context.method, method = delegate.iterator[methodName]; if (undefined === method) return context.delegate = null, "throw" === methodName && delegate.iterator["return"] && (context.method = "return", context.arg = undefined, maybeInvokeDelegate(delegate, context), "throw" === context.method) || "return" !== methodName && (context.method = "throw", context.arg = new TypeError("The iterator does not provide a '" + methodName + "' method")), ContinueSentinel; var record = tryCatch(method, delegate.iterator, context.arg); if ("throw" === record.type) return context.method = "throw", context.arg = record.arg, context.delegate = null, ContinueSentinel; var info = record.arg; return info ? info.done ? (context[delegate.resultName] = info.value, context.next = delegate.nextLoc, "return" !== context.method && (context.method = "next", context.arg = undefined), context.delegate = null, ContinueSentinel) : info : (context.method = "throw", context.arg = new TypeError("iterator result is not an object"), context.delegate = null, ContinueSentinel); } function pushTryEntry(locs) { var entry = { tryLoc: locs[0] }; 1 in locs && (entry.catchLoc = locs[1]), 2 in locs && (entry.finallyLoc = locs[2], entry.afterLoc = locs[3]), this.tryEntries.push(entry); } function resetTryEntry(entry) { var record = entry.completion || {}; record.type = "normal", delete record.arg, entry.completion = record; } function Context(tryLocsList) { this.tryEntries = [{ tryLoc: "root" }], tryLocsList.forEach(pushTryEntry, this), this.reset(!0); } function values(iterable) { if (iterable) { var iteratorMethod = iterable[iteratorSymbol]; if (iteratorMethod) return iteratorMethod.call(iterable); if ("function" == typeof iterable.next) return iterable; if (!isNaN(iterable.length)) { var i = -1, next = function next() { for (; ++i < iterable.length;) if (hasOwn.call(iterable, i)) return next.value = iterable[i], next.done = !1, next; return next.value = undefined, next.done = !0, next; }; return next.next = next; } } return { next: doneResult }; } function doneResult() { return { value: undefined, done: !0 }; } return GeneratorFunction.prototype = GeneratorFunctionPrototype, defineProperty(Gp, "constructor", { value: GeneratorFunctionPrototype, configurable: !0 }), defineProperty(GeneratorFunctionPrototype, "constructor", { value: GeneratorFunction, configurable: !0 }), GeneratorFunction.displayName = define(GeneratorFunctionPrototype, toStringTagSymbol, "GeneratorFunction"), exports.isGeneratorFunction = function (genFun) { var ctor = "function" == typeof genFun && genFun.constructor; return !!ctor && (ctor === GeneratorFunction || "GeneratorFunction" === (ctor.displayName || ctor.name)); }, exports.mark = function (genFun) { return Object.setPrototypeOf ? Object.setPrototypeOf(genFun, GeneratorFunctionPrototype) : (genFun.__proto__ = GeneratorFunctionPrototype, define(genFun, toStringTagSymbol, "GeneratorFunction")), genFun.prototype = Object.create(Gp), genFun; }, exports.awrap = function (arg) { return { __await: arg }; }, defineIteratorMethods(AsyncIterator.prototype), define(AsyncIterator.prototype, asyncIteratorSymbol, function () { return this; }), exports.AsyncIterator = AsyncIterator, exports.async = function (innerFn, outerFn, self, tryLocsList, PromiseImpl) { void 0 === PromiseImpl && (PromiseImpl = Promise); var iter = new AsyncIterator(wrap(innerFn, outerFn, self, tryLocsList), PromiseImpl); return exports.isGeneratorFunction(outerFn) ? iter : iter.next().then(function (result) { return result.done ? result.value : iter.next(); }); }, defineIteratorMethods(Gp), define(Gp, toStringTagSymbol, "Generator"), define(Gp, iteratorSymbol, function () { return this; }), define(Gp, "toString", function () { return "[object Generator]"; }), exports.keys = function (val) { var object = Object(val), keys = []; for (var key in object) keys.push(key); return keys.reverse(), function next() { for (; keys.length;) { var key = keys.pop(); if (key in object) return next.value = key, next.done = !1, next; } return next.done = !0, next; }; }, exports.values = values, Context.prototype = { constructor: Context, reset: function reset(skipTempReset) { if (this.prev = 0, this.next = 0, this.sent = this._sent = undefined, this.done = !1, this.delegate = null, this.method = "next", this.arg = undefined, this.tryEntries.forEach(resetTryEntry), !skipTempReset) for (var name in this) "t" === name.charAt(0) && hasOwn.call(this, name) && !isNaN(+name.slice(1)) && (this[name] = undefined); }, stop: function stop() { this.done = !0; var rootRecord = this.tryEntries[0].completion; if ("throw" === rootRecord.type) throw rootRecord.arg; return this.rval; }, dispatchException: function dispatchException(exception) { if (this.done) throw exception; var context = this; function handle(loc, caught) { return record.type = "throw", record.arg = exception, context.next = loc, caught && (context.method = "next", context.arg = undefined), !!caught; } for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i], record = entry.completion; if ("root" === entry.tryLoc) return handle("end"); if (entry.tryLoc <= this.prev) { var hasCatch = hasOwn.call(entry, "catchLoc"), hasFinally = hasOwn.call(entry, "finallyLoc"); if (hasCatch && hasFinally) { if (this.prev < entry.catchLoc) return handle(entry.catchLoc, !0); if (this.prev < entry.finallyLoc) return handle(entry.finallyLoc); } else if (hasCatch) { if (this.prev < entry.catchLoc) return handle(entry.catchLoc, !0); } else { if (!hasFinally) throw new Error("try statement without catch or finally"); if (this.prev < entry.finallyLoc) return handle(entry.finallyLoc); } } } }, abrupt: function abrupt(type, arg) { for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i]; if (entry.tryLoc <= this.prev && hasOwn.call(entry, "finallyLoc") && this.prev < entry.finallyLoc) { var finallyEntry = entry; break; } } finallyEntry && ("break" === type || "continue" === type) && finallyEntry.tryLoc <= arg && arg <= finallyEntry.finallyLoc && (finallyEntry = null); var record = finallyEntry ? finallyEntry.completion : {}; return record.type = type, record.arg = arg, finallyEntry ? (this.method = "next", this.next = finallyEntry.finallyLoc, ContinueSentinel) : this.complete(record); }, complete: function complete(record, afterLoc) { if ("throw" === record.type) throw record.arg; return "break" === record.type || "continue" === record.type ? this.next = record.arg : "return" === record.type ? (this.rval = this.arg = record.arg, this.method = "return", this.next = "end") : "normal" === record.type && afterLoc && (this.next = afterLoc), ContinueSentinel; }, finish: function finish(finallyLoc) { for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i]; if (entry.finallyLoc === finallyLoc) return this.complete(entry.completion, entry.afterLoc), resetTryEntry(entry), ContinueSentinel; } }, "catch": function _catch(tryLoc) { for (var i = this.tryEntries.length - 1; i >= 0; --i) { var entry = this.tryEntries[i]; if (entry.tryLoc === tryLoc) { var record = entry.completion; if ("throw" === record.type) { var thrown = record.arg; resetTryEntry(entry); } return thrown; } } throw new Error("illegal catch attempt"); }, delegateYield: function delegateYield(iterable, resultName, nextLoc) { return this.delegate = { iterator: values(iterable), resultName: resultName, nextLoc: nextLoc }, "next" === this.method && (this.arg = undefined), ContinueSentinel; } }, exports; }
function asyncGeneratorStep(gen, resolve, reject, _next, _throw, key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { Promise.resolve(value).then(_next, _throw); } }
function _asyncToGenerator(fn) { return function () { var self = this, args = arguments; return new Promise(function (resolve, reject) { var gen = fn.apply(self, args); function _next(value) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "next", value); } function _throw(err) { asyncGeneratorStep(gen, resolve, reject, _next, _throw, "throw", err); } _next(undefined); }); }; }
// Counup npm library for the countup animation


// Get slideColors from the JSON
fetch('/static/js/slideColors.json').then(function (response) {
  return response.json();
}).then(function (json) {
  return main(json);
});
function main(_x) {
  return _main.apply(this, arguments);
}
function _main() {
  _main = _asyncToGenerator( /*#__PURE__*/_regeneratorRuntime().mark(function _callee(slideColors) {
    var startFromSlide, coinNavigation, slideIndex, app, slides, coins, findTheTruth, colorIndex, startSlide, amountOfSlides, coinsWidth, coinLeftRemValue, startScreenAnimation, initiateCoins, changeSlide, centerCoins;
    return _regeneratorRuntime().wrap(function _callee$(_context) {
      while (1) switch (_context.prev = _context.next) {
        case 0:
          centerCoins = function _centerCoins() {
            // Center the coins at the bottom of the slide again after the width is adjusted (one coin dissapeared)
            coinLeftRemValue = (36 - (coins.length - slideIndex) * 4) / 2 - 0.4;
            for (var i = slideIndex; i < coins.length; i++) {
              coins[i].style.left = coinLeftRemValue + "rem";
              coinLeftRemValue += 4;
            }
          };
          changeSlide = function _changeSlide() {
            // Next color
            colorIndex++;

            // Get new slideColors
            if (colorIndex >= slideColors.length) colorIndex = 0;
            var slideColor = slideColors[colorIndex];

            // Hide the coin that represents the next slide
            if (coins[slideIndex - startFromSlide]) coins[slideIndex - startFromSlide].style.left = -64 + "rem";

            // Change the background and front colors of each slide
            document.body.style.backgroundColor = slideColor.background;
            document.getElementById("slide-backfigure").style.backgroundColor = slideColor.main;

            // Up the variable so it represents the next slide
            slideIndex++;

            // Show the next slide using a negative margin
            startSlide.style.marginLeft = slideIndex * -36 + "rem";
            switch (slides[slideIndex].id) {
              case "date-most-ticket-sales":
                setTimeout(function () {
                  // Start the calander animation
                  document.getElementById("calander-illustration").classList.add("calander--normal");
                  setTimeout(function () {
                    return document.getElementsByClassName("date")[0].classList.add("date--show");
                  }, 1000);
                }, 1750);
                break;
              case "ticket-sale-percentage":
                // Initiate the countup animation on the ticket percentage slide
                new countup_js__WEBPACK_IMPORTED_MODULE_0__.CountUp(document.getElementById("ticketPercentageCountUp"), 95, {
                  duration: 3
                }).start();
                break;
              case "visitor-origins":
                // Initiate the countup animation on the visitor origins page
                new countup_js__WEBPACK_IMPORTED_MODULE_0__.CountUp(document.getElementById("visitorOriginsPercentageCountUp"), 95, {
                  duration: 3
                }).start();
                break;
              case "end-overview":
                // Hide logo on share screen
                document.getElementsByClassName("logo")[0].style.display = "none";

                // Remove the coins and backslide on the last screen for the final overview
                document.getElementById("slide-backfigure").classList.remove("slide__backfigure--visible");
                coins[coins.length - 1].style.top = 80 + "rem";
                break;
            }
            centerCoins();
          };
          initiateCoins = function _initiateCoins() {
            // Animate bottom slide
            if (coinNavigation) document.getElementById("slide-backfigure").classList.add("slide__backfigure--visible");

            // Add all coins to array
            if (coinNavigation) {
              coins[0].style.display = "block";
              for (var i = 0; i < amountOfSlides - slideIndex - 2; i++) {
                var coin = app.appendChild(coins[0].cloneNode(true));
                coin.style.display = "block";
                coins.push(coin);
              }
            }
            setTimeout(function () {
              var _loop = function _loop(_i2) {
                setTimeout(function () {
                  var coin = coins[_i2];
                  coin.style.top = 67 + "rem";
                  coin.style.left = coinLeftRemValue + "rem";
                  coinLeftRemValue += 4;

                  // Let every second coin slide down so they are paired
                  if (_i2 % 2) coin.style.top = parseInt(coin.style.top.slice(0, -3)) + 1.25 + "rem";

                  // Give the coins a different CSS transition (time)
                  setTimeout(function () {
                    return coin.style.transition = "left .75s ease-in-out, top 2s ease-in-out";
                  }, 2000);
                }, 50 * _i2);
              };
              // Position every coin centered at the bottom of the screen
              for (var _i2 = 0; _i2 < coins.length; _i2++) {
                _loop(_i2);
              }

              // Change slide on click
              for (var _i3 = 0; _i3 < slides.length; _i3++) if (slides[_i3].id != "find-the-truth") slides[_i3].addEventListener("click", changeSlide);
            }, 250);
          };
          startScreenAnimation = function _startScreenAnimation() {
            // Hide clickabe cursor
            startSlide.style.cursor = "initial";

            // Hide the text before starting the plug animation
            document.getElementById("begin-bottom").classList.add("title--hide");
            setTimeout(function () {
              // Start the plug animation
              document.getElementById("plug").classList.add("active");
              setTimeout(function () {
                return document.getElementsByClassName("begin-illustration")[0].classList.add("begin-illustration--start");
              }, 1000);
              setTimeout(function () {
                // Pull the lever downwards with a CSS class
                document.getElementsByClassName("lever")[0].classList.add("lever--active");

                // Animate coins and bottom slide
                initiateCoins();
              }, 2750);
            }, 750);
          };
          // Data variables
          startFromSlide = 0;
          coinNavigation = true;
          slideIndex = startFromSlide; // Element variables
          app = document.getElementById("app");
          slides = document.getElementsByClassName("slide");
          coins = [document.getElementsByClassName("coin")[0]];
          findTheTruth = document.getElementById("find-the-truth-form"); // Summary slide related variables
          colorIndex = 0;
          startSlide = slides[0];
          amountOfSlides = slides.length; // Calculate the left value so the coins are centered when placed
          coinsWidth = (amountOfSlides - slideIndex - 1) * 4;
          coinLeftRemValue = (36 - coinsWidth) / 2 - 0.4; // Determine from which slide to start and start the summary accordingly
          if (startFromSlide === 0) startSlide.addEventListener("click", startScreenAnimation, {
            once: true
          });else {
            initiateCoins();
            if (!coinNavigation) startSlide.style.transition = "none";
            startSlide.style.marginLeft = slideIndex * -36 + "rem";
          }

          // When submitting the find the truth component
          findTheTruth.addEventListener("submit", function (e) {
            // Stop the regular submitting of the form
            e.preventDefault();

            // Variables
            var button = findTheTruth.getElementsByClassName("btn")[0];
            var statements = findTheTruth.getElementsByClassName("statements")[0].children;

            // Hide the button after submuitting
            button.style.translate = "36rem 0";

            // Show the searchglass illustation
            findTheTruth.getElementsByClassName("search-glass")[0].style.bottom = "4.5rem";

            // Give error classes to all statements
            for (var i = 0; i < statements.length; i++) statements[i].classList.add("statement--error");

            // Give the right statement the right class (hardcoded for now)
            statements[0].classList.add("statement--check");

            // Eventlistener to show the slide with validation of the statemnt
            document.getElementById("find-the-truth").addEventListener("click", function () {
              // Hide all answers that are not the right one or clarification
              for (var _i = 0; _i < statements.length; _i++) if (!statements[_i].classList.contains("statement--check")) statements[_i].style.display = "none";

              // Hide the search glass illustration
              findTheTruth.getElementsByClassName("search-glass")[0].style.bottom = "-20rem";

              // Show the correctionbox with the celebratory illustration
              setTimeout(function () {
                findTheTruth.getElementsByClassName("correction-box")[0].classList.add("correction-box--active");
                findTheTruth.getElementsByClassName("celebrate")[0].classList.add("celebrate--active");
              }, 500);

              // Go the next slide when clicking on the current slide
              setTimeout(function () {
                return document.getElementById("find-the-truth").addEventListener("click", changeSlide);
              }, 1000);
            });
          });
        case 18:
        case "end":
          return _context.stop();
      }
    }, _callee);
  }));
  return _main.apply(this, arguments);
}

/***/ }),

/***/ "./node_modules/countup.js/dist/countUp.min.js":
/*!*****************************************************!*\
  !*** ./node_modules/countup.js/dist/countUp.min.js ***!
  \*****************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
/* harmony export */ __webpack_require__.d(__webpack_exports__, {
/* harmony export */   CountUp: () => (/* binding */ i)
/* harmony export */ });
var t=function(){return t=Object.assign||function(t){for(var i,n=1,s=arguments.length;n<s;n++)for(var a in i=arguments[n])Object.prototype.hasOwnProperty.call(i,a)&&(t[a]=i[a]);return t},t.apply(this,arguments)},i=function(){function i(i,n,s){var a=this;this.endVal=n,this.options=s,this.version="2.6.2",this.defaults={startVal:0,decimalPlaces:0,duration:2,useEasing:!0,useGrouping:!0,useIndianSeparators:!1,smartEasingThreshold:999,smartEasingAmount:333,separator:",",decimal:".",prefix:"",suffix:"",enableScrollSpy:!1,scrollSpyDelay:200,scrollSpyOnce:!1},this.finalEndVal=null,this.useEasing=!0,this.countDown=!1,this.error="",this.startVal=0,this.paused=!0,this.once=!1,this.count=function(t){a.startTime||(a.startTime=t);var i=t-a.startTime;a.remaining=a.duration-i,a.useEasing?a.countDown?a.frameVal=a.startVal-a.easingFn(i,0,a.startVal-a.endVal,a.duration):a.frameVal=a.easingFn(i,a.startVal,a.endVal-a.startVal,a.duration):a.frameVal=a.startVal+(a.endVal-a.startVal)*(i/a.duration);var n=a.countDown?a.frameVal<a.endVal:a.frameVal>a.endVal;a.frameVal=n?a.endVal:a.frameVal,a.frameVal=Number(a.frameVal.toFixed(a.options.decimalPlaces)),a.printValue(a.frameVal),i<a.duration?a.rAF=requestAnimationFrame(a.count):null!==a.finalEndVal?a.update(a.finalEndVal):a.options.onCompleteCallback&&a.options.onCompleteCallback()},this.formatNumber=function(t){var i,n,s,e,o=t<0?"-":"";i=Math.abs(t).toFixed(a.options.decimalPlaces);var r=(i+="").split(".");if(n=r[0],s=r.length>1?a.options.decimal+r[1]:"",a.options.useGrouping){e="";for(var l=3,h=0,u=0,p=n.length;u<p;++u)a.options.useIndianSeparators&&4===u&&(l=2,h=1),0!==u&&h%l==0&&(e=a.options.separator+e),h++,e=n[p-u-1]+e;n=e}return a.options.numerals&&a.options.numerals.length&&(n=n.replace(/[0-9]/g,(function(t){return a.options.numerals[+t]})),s=s.replace(/[0-9]/g,(function(t){return a.options.numerals[+t]}))),o+a.options.prefix+n+s+a.options.suffix},this.easeOutExpo=function(t,i,n,s){return n*(1-Math.pow(2,-10*t/s))*1024/1023+i},this.options=t(t({},this.defaults),s),this.formattingFn=this.options.formattingFn?this.options.formattingFn:this.formatNumber,this.easingFn=this.options.easingFn?this.options.easingFn:this.easeOutExpo,this.startVal=this.validateValue(this.options.startVal),this.frameVal=this.startVal,this.endVal=this.validateValue(n),this.options.decimalPlaces=Math.max(this.options.decimalPlaces),this.resetDuration(),this.options.separator=String(this.options.separator),this.useEasing=this.options.useEasing,""===this.options.separator&&(this.options.useGrouping=!1),this.el="string"==typeof i?document.getElementById(i):i,this.el?this.printValue(this.startVal):this.error="[CountUp] target is null or undefined","undefined"!=typeof window&&this.options.enableScrollSpy&&(this.error?console.error(this.error,i):(window.onScrollFns=window.onScrollFns||[],window.onScrollFns.push((function(){return a.handleScroll(a)})),window.onscroll=function(){window.onScrollFns.forEach((function(t){return t()}))},this.handleScroll(this)))}return i.prototype.handleScroll=function(t){if(t&&window&&!t.once){var i=window.innerHeight+window.scrollY,n=t.el.getBoundingClientRect(),s=n.top+window.pageYOffset,a=n.top+n.height+window.pageYOffset;a<i&&a>window.scrollY&&t.paused?(t.paused=!1,setTimeout((function(){return t.start()}),t.options.scrollSpyDelay),t.options.scrollSpyOnce&&(t.once=!0)):(window.scrollY>a||s>i)&&!t.paused&&t.reset()}},i.prototype.determineDirectionAndSmartEasing=function(){var t=this.finalEndVal?this.finalEndVal:this.endVal;this.countDown=this.startVal>t;var i=t-this.startVal;if(Math.abs(i)>this.options.smartEasingThreshold&&this.options.useEasing){this.finalEndVal=t;var n=this.countDown?1:-1;this.endVal=t+n*this.options.smartEasingAmount,this.duration=this.duration/2}else this.endVal=t,this.finalEndVal=null;null!==this.finalEndVal?this.useEasing=!1:this.useEasing=this.options.useEasing},i.prototype.start=function(t){this.error||(t&&(this.options.onCompleteCallback=t),this.duration>0?(this.determineDirectionAndSmartEasing(),this.paused=!1,this.rAF=requestAnimationFrame(this.count)):this.printValue(this.endVal))},i.prototype.pauseResume=function(){this.paused?(this.startTime=null,this.duration=this.remaining,this.startVal=this.frameVal,this.determineDirectionAndSmartEasing(),this.rAF=requestAnimationFrame(this.count)):cancelAnimationFrame(this.rAF),this.paused=!this.paused},i.prototype.reset=function(){cancelAnimationFrame(this.rAF),this.paused=!0,this.resetDuration(),this.startVal=this.validateValue(this.options.startVal),this.frameVal=this.startVal,this.printValue(this.startVal)},i.prototype.update=function(t){cancelAnimationFrame(this.rAF),this.startTime=null,this.endVal=this.validateValue(t),this.endVal!==this.frameVal&&(this.startVal=this.frameVal,null==this.finalEndVal&&this.resetDuration(),this.finalEndVal=null,this.determineDirectionAndSmartEasing(),this.rAF=requestAnimationFrame(this.count))},i.prototype.printValue=function(t){var i;if(this.el){var n=this.formattingFn(t);if(null===(i=this.options.plugin)||void 0===i?void 0:i.render)this.options.plugin.render(this.el,n);else if("INPUT"===this.el.tagName)this.el.value=n;else"text"===this.el.tagName||"tspan"===this.el.tagName?this.el.textContent=n:this.el.innerHTML=n}},i.prototype.ensureNumber=function(t){return"number"==typeof t&&!isNaN(t)},i.prototype.validateValue=function(t){var i=Number(t);return this.ensureNumber(i)?i:(this.error="[CountUp] invalid start or end value: ".concat(t),null)},i.prototype.resetDuration=function(){this.startTime=null,this.duration=1e3*Number(this.options.duration),this.remaining=this.duration},i}();


/***/ }),

/***/ "./EventixPrj/EventixApp/resources/sass/stylesheet.sass":
/*!**************************************************************!*\
  !*** ./EventixPrj/EventixApp/resources/sass/stylesheet.sass ***!
  \**************************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

__webpack_require__.r(__webpack_exports__);
// extracted by mini-css-extract-plugin


/***/ }),

/***/ "./EventixPrj/EventixApp/resources/sass/xrDemo.sass":
/*!**********************************************************!*\
  !*** ./EventixPrj/EventixApp/resources/sass/xrDemo.sass ***!
  \**********************************************************/
/***/ ((__unused_webpack_module, __webpack_exports__, __webpack_require__) => {

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
/******/ 	/* webpack/runtime/define property getters */
/******/ 	(() => {
/******/ 		// define getter functions for harmony exports
/******/ 		__webpack_require__.d = (exports, definition) => {
/******/ 			for(var key in definition) {
/******/ 				if(__webpack_require__.o(definition, key) && !__webpack_require__.o(exports, key)) {
/******/ 					Object.defineProperty(exports, key, { enumerable: true, get: definition[key] });
/******/ 				}
/******/ 			}
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
/******/ 			"EventixPrj/EventixApp/static/css/xrDemo": 0,
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
/******/ 	__webpack_require__.O(undefined, ["EventixPrj/EventixApp/static/css/xrDemo","EventixPrj/EventixApp/static/css/stylesheet"], () => (__webpack_require__("./EventixPrj/EventixApp/resources/js/main.js")))
/******/ 	__webpack_require__.O(undefined, ["EventixPrj/EventixApp/static/css/xrDemo","EventixPrj/EventixApp/static/css/stylesheet"], () => (__webpack_require__("./EventixPrj/EventixApp/resources/sass/stylesheet.sass")))
/******/ 	var __webpack_exports__ = __webpack_require__.O(undefined, ["EventixPrj/EventixApp/static/css/xrDemo","EventixPrj/EventixApp/static/css/stylesheet"], () => (__webpack_require__("./EventixPrj/EventixApp/resources/sass/xrDemo.sass")))
/******/ 	__webpack_exports__ = __webpack_require__.O(__webpack_exports__);
/******/ 	
/******/ })()
;