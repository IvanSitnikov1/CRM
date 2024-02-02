<template>
      <article class="select-wrap"
               v-if="source.length"
               @touchstart.prevent="handleTouchStart"
               @touchmove.prevent="handleTouchMove"
               @touchend.prevent="handleTouchEnd">
        <ul class="select-options"
            :style="`transform: translate3d(0, 0, ${-radius}px) rotateX(${itemAngle * store.scroll}deg);`">
          <li
            v-for="(item, index) in source"
            :key="index"
            class="select-option"
            :style="`top: ${itemHeight * -0.5}px;
                height: ${itemHeight}px;
                line-height: ${itemHeight}px;
                transform: rotateX(${-itemAngle * index}deg) translate3d(0, 0, ${radius}px);`"
            :data-index="index"
            v-show="isWithinRange(index)"
          >
            {{ item.text }}
          </li>
        </ul>
        <div class="highlight"
             :style="`height: ${itemHeight}px;
                 line-height: ${itemHeight}px;`">
          <ul class="highlight-list"
              :style="`top: -${itemHeight}px; transform: translate3d(0, ${-store.scroll * itemHeight}px, 0);`">
            <li
              class="highlight-item"
              :style="`height: ${itemHeight}px`"
            >
              {{ source[source.length - 1].text }}
            </li>
            <li
              v-for="(item, index) in source"
              :key="index"
              class="highlight-item"
              :style="`height: ${itemHeight}px;`"
            >
              {{ item.text }}
            </li>
            <li
              class="highlight-item"
              :style="`height: ${itemHeight}px;`"
            >
              {{ source[0].text }}
            </li>
          </ul>
        </div>
      </article>
</template>

<script setup>

const easing = {
  easeOutCubic: (pos) => Math.pow(pos - 1, 3) + 1,
  easeOutQuart: (pos) => -(Math.pow(pos - 1, 4) - 1),
};

const generateHours = () => new Array(24).fill(1).map((v, i) => {
  return { value: i + 1, text: i + 1}
});
// todo props
const count = 20
const sensitivity = 0.8

const source = generateHours();
const itemHeight = 40;
const itemAngle = 360 / source.length;
const radius = itemHeight / Math.tan((itemAngle * Math.PI) / 180);
const a = sensitivity * 10;
const quarterCount = count / 4;

const isWithinRange = (index) => {
  const sourceLength = source.length;
  const distanceToScroll = Math.abs(index - store.scroll);
  const distanceToScrollEnd = Math.abs(index - store.scroll - sourceLength);
  const distanceToScrollBeginning = Math.abs(index - store.scroll + sourceLength);

  return (
    distanceToScroll < quarterCount ||
    distanceToScrollEnd < quarterCount ||
    distanceToScrollBeginning < quarterCount
  );
};
const handleTouchStart = (e) => {
  const eventY = e.clientY || e.touches[0].clientY;
  store.touchData.startY = eventY;
  store.touchData.yArr = [[eventY, new Date().getTime()]];
  store.touchData.touchScroll = store.scroll;
  stop();
};

const handleTouchMove = (e) => {
  const eventY = e.clientY || e.touches[0].clientY;
  store.touchData.yArr.push([eventY, new Date().getTime()]);
  const scrollAdd = (store.touchData.startY - eventY) / (itemHeight * 20);
  const moveToScroll = scrollAdd + store.scroll;
  console.log(moveToScroll)
  store.scroll = normalizeScroll(moveToScroll);
  store.touchData.touchScroll = normalizeScroll(moveToScroll);
};
const handleTouchEnd = () => {
  let v = 0;

  if (store.touchData.yArr.length > 1) {
    const [prevY, prevTime] = store.touchData.yArr[store.touchData.yArr.length - 2];
    const [currentY, currentTime] = store.touchData.yArr[store.touchData.yArr.length - 1];

    const deltaY = currentY - prevY;
    const deltaTime = currentTime - prevTime;

    v = (deltaY / itemHeight) * 1000 / deltaTime;
    v = Math.min(Math.abs(v), 30) * Math.sign(v); // Ensure v is within the range [-30, 30]
  }
  store.scroll = store.touchData.touchScroll;
  animateMoveByInitV(-v)
};
// If you have more logic for the component, you can add it here
const store = reactive({
  selected: null,
  moveT: 0,
  touchData: {
    startY: 0,
    yArr: [],
    touchScroll: 0,
  },
  moving: false,
  scroll: 0,
});

const normalizeScroll = (scroll) => {
  let normalizedScroll = scroll;

  while (normalizedScroll < 0) {
    normalizedScroll += source.length;
  }
  return normalizedScroll % source.length;
};

const animateMoveByInitV = async (initV) => {
  const acceleration = initV > 0 ? -a : a; // Deceleration or acceleration
  const time = Math.abs(initV / acceleration); // Time to reduce speed to 0
  const totalScrollLen = initV * time + (acceleration * time * time) / 2; // Total scrolling distance
  const finalScroll = Math.round(store.scroll + totalScrollLen); // Round to ensure final scroll is an integer

  await animateToScroll(store.scroll, finalScroll, time, 'easeOutQuart');
 /* selectByScroll(store.scroll);*/
};

const animateToScroll = (initScroll, finalScroll, time, easingName = "easeOutQuart") => {
  if (initScroll === finalScroll || time === 0) {
    return;
  }

  const startTime = new Date().getTime() / 1000;
  let pass = 0;
  const totalScrollLen = finalScroll - initScroll;

  return new Promise((resolve) => {
    store.moving = true;
    const tick = () => {
      pass = new Date().getTime() / 1000 - startTime;
      if (pass < time) {
        const progress = pass / time;
        store.scroll = normalizeScroll(initScroll + easing[easingName](progress) * totalScrollLen);
        store.moveT = requestAnimationFrame(tick);
      } else {
        resolve();
        stop();
        store.scroll = normalizeScroll(initScroll + totalScrollLen);
      }
    };
    tick();
  });
};

const stop = () => {
  store.moving = false
  cancelAnimationFrame(store.moveT);
};

const selectByScroll = (scroll) => {
  // Call the _selectByScroll method with props.options and other properties from store
  // ...
};

const select = (value) => {
  // Call the select method with props.options and other properties from store
  // ...
};
</script>

<style lang="scss">
  @import "style.module";
</style>
