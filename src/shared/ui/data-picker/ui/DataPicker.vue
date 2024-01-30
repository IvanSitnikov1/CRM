<template>
  <article class="calendar">
      <header class="calendar__header">
        <Title class="calendar__title" :data="{
          title: 'September, 2020',
          size: 'medium',
          isHighLeading: true
        }"/>
        <img src="@/shared/assets/icons/arrowLeftLong.svg" alt="left" class="calendar__arrow_left">
        <img src="@/shared/assets/icons/arrowRightLong.svg" alt="arrow" class="calendar__arrow_right">
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
        <tbody class="calendar__month">
          <tr class="calendar__days">
            <td class="calendar__day calendar__day_prev-month">26</td>
            <td class="calendar__day calendar__day_prev-month">27</td>
            <td class="calendar__day calendar__day_prev-month">28</td>
            <td class="calendar__day calendar__day_prev-month">29</td>
            <td class="calendar__day calendar__day_prev-month">30</td>
          </tr>

          <tr class="calendar__days" v-for="index in 2" :key="index">
            <td class="calendar__day">2</td>
            <td class="calendar__day calendar__day_event">3</td>
            <td class="calendar__day">4</td>
            <td class="calendar__day">5</td>
            <td class="calendar__day">6</td>
          </tr>

          <tr class="calendar__days">
            <td class="calendar__day calendar__day_selected">2</td>
            <td class="calendar__day">3</td>
            <td class="calendar__day">4</td>
            <td class="calendar__day">5</td>
            <td class="calendar__day">6</td>
          </tr>

          <tr class="calendar__days">
            <td class="calendar__day calendar__day_next-month">26</td>
            <td class="calendar__day calendar__day_next-month">27</td>
            <td class="calendar__day calendar__day_next-month">28</td>
            <td class="calendar__day calendar__day_next-month">29</td>
            <td class="calendar__day calendar__day_next-month">30</td>
          </tr>
        </tbody>
      </table>
      <hr class="calendar__line">
  </article>
</template>

<script setup lang="ts">
import { type ILink } from '../../link'
import { Title } from '@/shared/ui/title'

const props = defineProps<{
  data: ILink
}>()


</script>

<style lang="scss">
 @import "style.module";
</style>
