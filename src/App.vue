<template>
  <div class="top">
    <div class="left">
      <div class="title">
        <div class="name">
          <img class="logo_img" src="@/assets/icon.png" alt="One Piece Logo" />
          <h1>
            <span style="color: var(--primary)">Piece</span>
            <span style="color: var(--c4)">Scheduler</span>
          </h1>
        </div>
      </div>
      <hr />
      <div class="selectors">
        <div class="range">
          <h2>Episode Range</h2>
          <input type="text" name="Episode Range" id="range" />
        </div>
        <div class="frequency">
          <h2>Frequency</h2>
          <form class="labels">
            <label for="weekly">
              <input
                type="radio"
                name="frequency"
                id="weekly"
                checked="checked"
              />
              Weekly
            </label>

            <label for="biweekly">
              <input type="radio" name="frequency" id="biweekly" /> Bi-Weekly
            </label>

            <label for="triweekly">
              <input type="radio" name="frequency" id="triweekly" /> Tri-Weekly
            </label>

            <label for="monthly">
              <input type="radio" name="frequency" id="monthly" /> Monthly
            </label>
          </form>
        </div>
        <div class="weekdays">
          <h2>Weekdays</h2>
          <form class="labels">
            <label for="monday">
              <input type="checkbox" name="weekdays" id="monday" /> M
            </label>
            <label for="tuesday">
              <input type="checkbox" name="weekdays" id="tuesday" /> T
            </label>
            <label for="wednesday">
              <input type="checkbox" name="weekdays" id="wednesday" /> W
            </label>
            <label for="thursday">
              <input type="checkbox" name="weekdays" id="thursday" /> Th
            </label>
            <label for="friday">
              <input type="checkbox" name="weekdays" id="friday" /> F
            </label>
            <label for="saturday">
              <input type="checkbox" name="weekdays" id="saturday" /> Sa
            </label>
            <label for="sunday">
              <input type="checkbox" name="weekdays" id="sunday" /> Su
            </label>
          </form>
        </div>
      </div>
    </div>
    <div class="right">
      <div class="calendar"></div>
      <div class="list"></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
};
</script>

<style>
:root {
  --primary: #c8472c;
  --c2: #4d5459;
  --c3: #508484;
  --c4: #c59849;
  --c5: #f4c095;
}

/* Top */

#app {
  height: 100%;
  width: 100%;
}

body {
  margin: 0;
  padding: 0;
  background-color: var(--c3);
  height: 100vh;
  width: 100vw;
}

.top {
  display: flex;
  flex-direction: row;
  height: 100%;
  width: 100%;
}

.left {
  width: 25vw;
  height: 100%;
  background-color: var(--c2);
}

.right {
  width: 75vw;
}

/* Left Side */

.logo_img {
  height: 100%;
  width: auto;
}

.name {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  height: 100%;
}

.name > h1 {
  font-size: 3em;
  padding: 5px;
  margin: 5px;
}

hr {
  color: var(--c4);
  width: 80%;
  height: 5px;
  border-width: 0;
  color: var(--c4);
  background-color: var(--c4);
  border-radius: 5px;
}

.selectors {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-evenly;
  height: 100%;
  width: 100%;
}

.range {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.frequency {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.labels {
  display: flex;
  flex-direction: column;
}

/* Right Side */

.calendar {
  width: 100%;
  height: 50%;
}

.list {
  width: 100%;
  height: 50%;
}
</style>
