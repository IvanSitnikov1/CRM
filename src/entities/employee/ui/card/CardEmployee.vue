<template>
  <section class="employee-card" :class="getEmployeeClasses">
    <article class="employee-card__header">
      <div class="employee-card__profile">
        <img class="employee-card__image" src="@/shared/assets/test.png" alt="profile">
      </div>
      <div class="employee-card__info">
        <Title :data="{
                  title: data.name,
                  isHighLeading: true,
                  size: 'small'
                }"/>
        <div class="employee-card__job">{{ data.job }}</div>
      </div>
    </article>
    <hr class="employee-card__line" v-show="data.isShowLine">
    <slot name="content"/>
  </section>
</template>

<script setup lang="ts">
import { type ICardEmployee } from './../../index'
import { Title } from '@/shared/ui/title'

const props = defineProps<{
  data: ICardEmployee
}>()

const getEmployeeClasses = computed(() => {
  return {
    'employee-card_border': props.data.isBorderRound,
    'employee-card_shadow': props.data.isShadow,
  };
});

</script>

<style lang="scss">
 @import "style.module";
</style>
