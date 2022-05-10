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
          <input
            type="text"
            class="colored_input"
            name="Episode Range"
            id="range"
            v-model="range"
          />
          <div class="filler_div">
            <input v-model="filler" type="checkbox" name="filler" id="filler" />
            <label for="filler">Include Filler</label>
          </div>
        </div>
        <div class="frequency">
          <h2>Frequency</h2>
          <form class="labels">
            <label class="frequency_label" for="weekly">
              <input
                type="radio"
                name="frequency"
                id="weekly"
                value="weekly"
                checked="checked"
                v-model="frequency"
              />
              Weekly
            </label>

            <label class="frequency_label" for="biweekly">
              <input
                type="radio"
                name="frequency"
                id="biweekly"
                value="biweekly"
                v-model="frequency"
              />
              Bi-Weekly
            </label>

            <label class="frequency_label" for="triweekly">
              <input
                type="radio"
                name="frequency"
                id="triweekly"
                value="triweekly"
                v-model="frequency"
              />
              Tri-Weekly
            </label>

            <label class="frequency_label" for="monthly">
              <input
                type="radio"
                name="frequency"
                id="monthly"
                value="monthly"
                v-model="frequency"
              />
              Monthly
            </label>
          </form>
        </div>
        <div class="weekdays">
          <h2>Weekdays</h2>
          <form class="dates">
            <label for="monday">
              <div class="date_choice">
                <input
                  type="checkbox"
                  name="weekdays"
                  id="monday"
                  value="monday"
                  @click="
                    () => {
                      selectDate('monday');
                    }
                  "
                />
                <p>M</p>
              </div>
            </label>
            <label for="tuesday">
              <div class="date_choice">
                <input
                  type="checkbox"
                  name="weekdays"
                  id="tuesday"
                  value="tuesday"
                  @click="
                    () => {
                      selectDate('tuesday');
                    }
                  "
                />
                <p>T</p>
              </div>
            </label>
            <label for="wednesday">
              <div class="date_choice">
                <input
                  type="checkbox"
                  name="weekdays"
                  id="wednesday"
                  value="wednesday"
                  @click="
                    () => {
                      selectDate('wednesday');
                    }
                  "
                />
                <p>W</p>
              </div>
            </label>
            <label for="thursday">
              <div class="date_choice">
                <input
                  type="checkbox"
                  name="weekdays"
                  id="thursday"
                  value="thursday"
                  @click="
                    () => {
                      selectDate('thursday');
                    }
                  "
                />
                <p>Th</p>
              </div>
            </label>
            <label for="friday">
              <div class="date_choice">
                <input
                  type="checkbox"
                  name="weekdays"
                  id="friday"
                  value="friday"
                  @click="
                    () => {
                      selectDate('friday');
                    }
                  "
                />
                <p>F</p>
              </div>
            </label>
            <label for="saturday">
              <div class="date_choice">
                <input
                  type="checkbox"
                  name="weekdays"
                  id="saturday"
                  value="saturday"
                  @click="
                    () => {
                      selectDate('saturday');
                    }
                  "
                />
                <p>Sa</p>
              </div>
            </label>
            <label for="sunday">
              <div class="date_choice">
                <input
                  type="checkbox"
                  name="weekdays"
                  id="sunday"
                  value="sunday"
                  @click="
                    () => {
                      selectDate('sunday');
                    }
                  "
                />
                <p>Su</p>
              </div>
            </label>
          </form>
        </div>

        <div class="hours">
          <h2>Hours Per Day</h2>
          <input v-model="hours" class="colored_input" type="text" />
        </div>
        <div class="end_date">
          <h2>End Date</h2>
          <input
            v-model="end_date"
            class="end_date_picker"
            type="date"
            name="end_date"
            id="end_date"
            :min="new Date().toISOString().split('T')[0]"
          />
        </div>
      </div>
    </div>
    <div class="right">
      <div class="calendar">
        <input type="button" value="Click to calculate" @click="calculate" />
      </div>
      <div class="list"></div>
    </div>
  </div>
</template>

<script>
import "v-calendar/dist/style.css";

import { episodes } from "@/assets/data.js";

export default {
  name: "App",
  components: {},
  data() {
    return {
      days: [],
      range: `1-${episodes.length}`,
      frequency: "weekly",
      hours: "1.0",
      end_date: "",
      filler: false,
    };
  },
  methods: {
    selectDate(date) {
      if (this.days.includes(date)) {
        this.days = this.days.filter((day) => day !== date);
      } else {
        this.days.push(date);
      }
    },
    calculate() {
      if (!this.range) {
        alert("Please enter a range");
        return;
      }
      if (!this.days.length) {
        alert("Please select at least one day");
        return;
      }
      if (!this.hours) {
        alert("Please enter hours per day");
        return;
      }
      if (!this.end_date) {
        alert("Please enter an end date");
        return;
      }

      let start_date = new Date();
      let end_date;
      try {
        end_date = new Date(this.end_date);
      } catch (e) {
        alert("Please enter a valid date.");
        return;
      }
      let hours;
      try {
        hours = parseFloat(this.hours);
      } catch (e) {
        alert("Please enter a valid number for hours.");
        return;
      }
      let included_episodes = [];
      let ranges = this.range.split(",");
      for (let range of ranges) {
        if (range.includes("-")) {
          let range_split = range.split("-");
          let start = Number(range_split[0] - 1);
          let end = Number(range_split[1]);
          if (this.filler) {
            included_episodes = included_episodes.concat(
              episodes.slice(start, end)
            );
          } else {
            included_episodes = included_episodes.concat(
              episodes.slice(start, end).filter((episode) => !episode.filler)
            );
          }
        } else {
          let episode = episodes[Number(range - 1)];
          if (episode && ((this.filler && episode.filler) || !this.filler)) {
            included_episodes.push(episode);
          }
        }
      }
      let total_seconds = included_episodes.reduce(
        (sum, episode) => sum + episode.duration,
        0
      );
      let total_hours = total_seconds / 3600;
      let hours_per_week = hours * this.days.length;
      let weeks = total_hours / hours_per_week;
      let weeks_between = weeksBetween(start_date, end_date);
      console.log(
        `Should take ${weeks} weeks with weeks between now and end date being ${weeks_between}`
      );
      if (weeks_between < weeks) {
        alert("You don't have enough time to complete this task.");
        return;
      } else {
        alert("You have enough time to complete this task.");
        return;
      }
    },
  },
};

function weeksBetween(d1, d2) {
  return (d2 - d1) / (7 * 24 * 60 * 60 * 1000);
}
</script>

<style>
:root {
  --primary: #c8472c;
  --c2: #4d5459;
  --c3: #508484;
  --c3-hover: #6b8c9c;
  --c4: #c59849;
  --c5: #f4c095;
}

/* Top */

#app {
  height: 100%;
  width: 100%;
  font: "Roboto", sans-serif;
  overflow: hidden;
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
  height: 100vh;
  background-color: var(--c2);
}

.right {
  width: 75vw;
  height: 100vh;
}

h2 {
  color: white;
}

/* Left Side */

.title {
  height: 4vh;
}

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
  height: 95vh;
  width: 100%;
}

.range {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.filler_div {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-top: 20px;
  font-size: 2em;
  color: var(--c4);
}

.colored_input {
  background-color: var(--c3);
  border: none;
  width: 50%;
  height: 50px;
  border-radius: 10px;
  color: white;
  font-size: 1em;
  padding: 0px 10px;
}

.frequency {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.frequency_label {
  font-size: 2.25em;
  color: var(--c4);
}

.weekdays {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.labels {
  display: flex;
  flex-direction: column;
}

.dates {
  display: flex;
  flex-direction: row;
}

.date_choice {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: var(--c3);
  border-radius: 50%;
  margin: 5px;
  width: 3.25rem;
  height: 3.25rem;
}

.date_choice:hover {
  background-color: var(--c3-hover);
}

.date_choice > p {
  padding: 0px;
  margin: 0px;
  z-index: 10000;
  user-select: none;
  color: var(--c4);
  font-size: 2rem;
}

.date_choice > input[type="checkbox"] {
  -webkit-appearance: none;
  appearance: none;
  background-color: transparent;
  margin: 0;
}

.date_choice > input[type="checkbox"]:checked ~ p {
  color: white;
}

.hours {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.end_date {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
}

.end_date_picker {
  background-color: var(--c3);
  border: none;
  width: 50%;
  height: 50px;
  border-radius: 10px;
  color: white;
  font-size: 2em;
  text-align: center;
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
