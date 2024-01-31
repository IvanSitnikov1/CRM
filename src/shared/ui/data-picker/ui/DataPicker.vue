<template>
  <article class="calendar">
    <header class="calendar__header" v-if="curentMonth">
      <transition name="fade" mode="out-in">
        <Title :key="curentMonth"
               class="calendar__title"
               :data="{
                  title: curentMonth,
                  size: 'medium',
                  isHighLeading: true
               }"
        />
      </transition>
      <img
        src="@/shared/assets/icons/arrowLeftLong.svg"
        alt="left"
        class="calendar__arrow_left"
        @click="calendar.goToPreviousMonth()"
      >
      <img
        src="@/shared/assets/icons/arrowRightLong.svg"
        alt="arrow"
        class="calendar__arrow_right"
        @click="calendar.goToNextMonth()"
      >
    </header>
    <table class="calendar__data">
      <thead>
      <tr class="calendar__days-name">
        <td class="calendar__day-name">Mon</td>
        <td class="calendar__day-name">Tue</td>
        <td class="calendar__day-name">Wen</td>
        <td class="calendar__day-name">Thu</td>
        <td class="calendar__day-name">Fri</td>
      </tr>
      </thead>
      <transition name="fade" mode="out-in">
        <tbody class="calendar__month" :key="curentDates">
        <tr v-for="(row, index) in curentDates" :key="index" class="calendar__days">
          <td v-for="date in row" :key="date.day" :class="getDateClasses(date)">
            {{ date.day }}
          </td>
        </tr>
        </tbody>
      </transition>
    </table>
    <hr class="calendar__line">
  </article>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue';
import { type ILink } from '../../link';
import { Title } from '@/shared/ui/title';
import { Calendar, DateInfo } from "./../index";

const calendar = reactive(new Calendar());
const curentDates = computed(() => calendar.getCalendar());
const curentMonth = computed(() => calendar.getCurrentMonth());

const getDateClasses = (date: DateInfo) => {
  return {
    'calendar__day': true,
    'calendar__day_prev-month': date.isPrevMonth,
    'calendar__day_selected': date.isSelected,
    'calendar__day_next-month': date.isNextMonth,
  };
};

const props = defineProps<{
  data: ILink
}>()

</script>


<style lang="scss">
 @import "style.module";
</style>
