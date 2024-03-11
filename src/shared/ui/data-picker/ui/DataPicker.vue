<template>
  <article class="date-picker">
    <header class="date-picker__header" v-if="curentMonth">
      <transition name="fade" mode="out-in">
        <Title :key="curentMonth"
               class="date-picker__title"
               ref="reference"
               :data="{
                  title: curentMonth,
                  size: 'medium',
                  isHighLeading: true
               }"
        />
      </transition>
      <IconBase
        class="date-picker__arrow_left"
        @click="calendar.goToPreviousMonth()"
        :data="{
          iconName: 'arrowLeftLong'
        }"/>
      <IconBase
        class="date-picker__arrow_right"
        @click="calendar.goToNextMonth()"
        :data="{
          iconName: 'arrowRightLong'
        }"/>
    </header>
    <table class="date-picker__data">
      <thead>
      <tr class="date-picker__days-name">
        <td class="date-picker__day-name">Mon</td>
        <td class="date-picker__day-name">Tue</td>
        <td class="date-picker__day-name">Wen</td>
        <td class="date-picker__day-name">Thu</td>
        <td class="date-picker__day-name">Fri</td>
      </tr>
      </thead>
      <transition name="fade" mode="out-in">
        <tbody class="date-picker__month" :key="curentMonth">
          <tr v-for="(row, index) in curentDates" :key="index" class="date-picker__days">
            <td v-for="date in row" :key="date.day" :class="getDateClasses(date)">
              {{ date.day }}
              <div class="date-picker__event"
                   v-for="index in getCountOfEventInDay(date.timestamp)"
                   :key="index"/>
            </td>
          </tr>
        </tbody>
      </transition>
    </table>
    <hr class="date-picker__line">
  </article>
</template>

<script setup lang="ts">
import { type IDatePicker } from '../../link'
import { Title } from '@/shared/ui/title';
import { Calendar, DateInfo } from "./../index";
import { IconBase } from '@/shared/ui/icon-base'
import { useFloating } from '@floating-ui/vue'

const reference = ref(null);
const floating = ref(null);
const {floatingStyles} = useFloating(reference, floating);

const calendar = reactive(new Calendar());
const curentDates = computed(() => calendar.getCalendar());
const curentMonth = computed(() => calendar.getCurrentMonth());

const getDateClasses = (date: DateInfo) => {
  return {
    'date-picker__day': true,
    'date-picker__day_prev-month': date.isPrevMonth,
    'date-picker__day_selected': date.isSelected,
    'date-picker__day_next-month': date.isNextMonth,
  };
};

const getCountOfEventInDay = (timestamp: number) => {
  if (props.data.events.has(timestamp)) {
    return props.data.events.get(timestamp)
  } else {
    return 0
  }
}

const props = defineProps<{
  data: IDatePicker
}>()

</script>


<style lang="scss">
 @import "style.module";
</style>
