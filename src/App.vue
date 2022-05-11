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
                value="0"
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
                value="1"
                v-model="frequency"
              />
              Bi-Weekly
            </label>
            <label class="frequency_label" for="triweekly">
              <input
                type="radio"
                name="frequency"
                id="triweekly"
                value="2"
                v-model="frequency"
              />
              Tri-Weekly
            </label>
            <label class="frequency_label" for="monthly">
              <input
                type="radio"
                name="frequency"
                id="monthly"
                value="3"
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
                      selectDate(1);
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
                      selectDate(2);
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
                      selectDate(3);
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
                      selectDate(4);
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
                      selectDate(5);
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
                      selectDate(6);
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
                      selectDate(0);
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
          <div class="check_end_date_div">
            <input
              type="checkbox"
              name="check_end_date"
              id="check_end_date"
              v-model="check_end"
            />
            <label for="check_end_date"
              ><p style="color: white">Check End Date?</p></label
            >
          </div>
          <div class="end_date" v-if="check_end">
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
        <input
          class="button"
          type="button"
          value="Click to Calculate"
          @click="calculate"
        />
      </div>
    </div>
    <div class="right">
      <div class="list">
        <h2 v-if="config">Selected Days</h2>
        <div class="selected_days" v-if="config">
          <div class="selected_days_li" v-for="day in config" :key="day[0]">
            <p class="selected_day_date">
              {{ day[0].toLocaleString().split(",")[0] }}
            </p>
            <div
              class="selected_day_info"
              v-for="episode in day[1]"
              :key="episode.mal_id"
            >
              <div class="selected_day_header">
                <h3 class="selected_day_title">{{ episode.title }}</h3>
                <p class="selected_day_runtime">
                  {{ Math.round((episode.duration / 60) * 100) / 100 }}m
                </p>
              </div>
              <div class="episode_info">
                <p class="selected_day_episode_number">
                  Episode {{ episode.mal_id }}
                </p>
                <a
                  href="https://www.animefillerlist.com/shows/one-piece"
                  target="_blank"
                  v-if="episode.filler"
                  class="red_text"
                  >FILLER</a
                >
                <a
                  href="https://www.animefillerlist.com/shows/one-piece"
                  target="_blank"
                  v-if="episode.recap"
                  class="red_text"
                  >RECAP</a
                >
                <a
                  href="https://www.animefillerlist.com/shows/one-piece"
                  target="_blank"
                  v-if="episode.mixed"
                  style="color: #0b3f6a"
                >
                  MIXED CANON/FILLER
                </a>
                <a
                  href="https://www.animefillerlist.com/shows/one-piece"
                  target="_blank"
                  v-if="episode.anime_canon"
                  style="color: black"
                  >Strictly Anime Canon</a
                >
              </div>

              <p class="selected_day_description">
                {{ episode.synopsis }}
              </p>
              <hr style="color: var(--c2); background-color: var(--c2)" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import "v-calendar/dist/style.css";

import { episodes } from "@/assets/data.js";

Date.prototype.addDays = function (days) {
  var date = new Date(this.valueOf());
  date.setDate(date.getDate() + days);
  return date;
};

export default {
  name: "App",
  components: {},
  data() {
    return {
      days: [],
      range: `1-${episodes.length}`,
      frequency: "0",
      hours: "1.0",
      end_date: "",
      filler: false,
      config: null,
      check_end: false,
    };
  },
  methods: {
    selectDate(date) {
      console.log(date);
      if (this.days.includes(date)) {
        this.days = this.days.filter((day) => day !== date);
      } else {
        this.days.push(date);
      }
      console.log(this.days);
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
      if (!this.end_date && this.check_end) {
        alert("Please enter an end date");
        return;
      }
      let frequency = parseInt(this.frequency);
      let start_date = new Date();
      let end_date;
      if (this.check_end) {
        try {
          end_date = new Date(this.end_date);
        } catch (e) {
          alert("Please enter a valid date.");
          return;
        }
      } else {
        end_date = new Date(8640000000000000);
      }
      let hours;
      try {
        hours = parseFloat(this.hours);
        if (hours > 24 || hours < 0) {
          throw new Error(
            "Hours per day cannot be greater than 24 or less than 0"
          );
        }
      } catch (e) {
        alert("Please enter a valid number for hours.");
        return;
      }
      let included_episodes = [];
      let ranges = this.range.split(",");
      for (let range of ranges) {
        if (range.includes("-")) {
          let range_split = range.split("-");
          if (range_split.length > 2) {
            alert(
              `Please enter a valid range. (Range ${range} had more than one '-')`
            );
            return;
          }
          let start_str = range_split[0];
          if (start_str == "") {
            alert(
              `Please enter a valid range. (Range ${range} included '-' but the left number was empty)`
            );
            return;
          }
          let start = parseInt(start_str) - 1;
          let end_str = range_split[1];
          if (end_str == "") {
            alert(
              `Please enter a valid range. (Range ${range} included '-' but the right number was empty)`
            );
            return;
          }
          let end = parseInt(end_str);
          if (end > episodes.length || start < 0) {
            alert(
              `Please enter a valid range. (Episode ${end} doesn't exist!)`
            );
            return;
          } else if (start > end) {
            alert(
              `Please enter a valid range. (Episode ${start} is after episode ${end})`
            );
            return;
          }
          included_episodes = included_episodes.concat(
            episodes
              .slice(start, end)
              .filter(
                (episode) =>
                  (!episode.filler || this.filler) &&
                  !included_episodes.includes(episode)
              )
          );
        } else {
          let index = parseInt(range) - 1;
          if (index > episodes.length || index < 0) {
            alert(
              `Please enter a valid range. (Episode ${index} doesn't exist!)`
            );
            return;
          }
          let episode = episodes[index];
          if (
            episode &&
            (!episode.filler || this.filler) &&
            !included_episodes.includes(episode)
          ) {
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
      let weeks = (total_hours / hours_per_week) * (frequency + 1);
      let weeks_between = weeksBetween(start_date, end_date);
      console.log(
        `Should take ${weeks} weeks with weeks between now and end date being ${weeks_between}`
      );
      if (weeks_between < weeks) {
        alert("You don't have enough time to complete this task.");
        return;
      }

      let days = [];
      let currentDay = start_date;
      let index = 0;
      while (currentDay <= end_date && index < included_episodes.length) {
        if (this.days.includes(currentDay.getDay())) {
          let current_episodes = [];
          let total_time = 0;
          while (total_time < hours && index < included_episodes.length) {
            let episode = included_episodes[index];
            let duration = episode.duration / 3600;
            if (duration + total_time <= hours) {
              current_episodes.push(episode);
              total_time += duration;
              index++;
            } else {
              break;
            }
          }
          days.push([currentDay, current_episodes]);
        }
        currentDay = currentDay.addDays(1);
        if (currentDay.getDay() === 0 && frequency > 0) {
          currentDay = currentDay.addDays(7 * frequency);
        }
      }
      console.log(days);
      this.config = days;
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
  width: 25%;
  height: 100%;
  background-color: var(--c2);
  overflow: scroll;
}

.right {
  width: 75%;
  height: 100%;
}

h2 {
  color: white;
}

.red_text {
  color: red;
}

/* Left Side */

.title {
  height: 4%;
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
  font-size: 150%;
  padding: 5px;
  margin: 5px;
}

hr {
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
  height: 96%;
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
  font-size: 100%;
  color: var(--c4);
}

.colored_input {
  background-color: var(--c3);
  border: none;
  width: 50%;
  height: 100%;
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
  font-size: 125%;
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
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  width: 100%;
}

.date_choice {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: var(--c3);
  border-radius: 50%;
  margin: 5px;
  width: 3.25em;
  height: 3.25em;
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
  font-size: 125%;
}

.date_choice > input[type="checkbox"] {
  -webkit-appearance: none;
  appearance: none;
  background-color: transparent;
  margin: 0;
}

.date_choice > input[type="checkbox"]:checked ~ p {
  color: white;
  transition-duration: 0.1s;
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

.check_end_date_div {
  display: flex;
  flex-direction: row;
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
  font-size: 125%;
  text-align: center;
}

.button {
  transition-duration: 0.1s;
  background-color: var(--c4);
  border: none;
  width: 25%;
  min-width: 125px;
  height: 50px;
  border-radius: 10px;
}

.button:hover {
  background-color: var(--primary); /* Green */
  color: white;
}

/* Right Side */

.list {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.selected_days {
  height: 100%;
  width: 80%;
  max-width: 80%;
  margin: 10px;
  overflow-y: scroll;
  overflow-x: hidden;
}

.selected_day_date {
  font-size: 1.25em;
  color: black;
}

.selected_days_li {
  padding: 2px;
  margin: 10px;
  background-color: var(--c5);
  border-radius: 10px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.selected_day_info {
  display: flex;
  flex-direction: column;
  padding: 10px;
  width: 90%;
}

.selected_day_header {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.episode_info {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
}
</style>
