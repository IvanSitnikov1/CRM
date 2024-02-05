<template>
  <article class="tab">
    <div class="tab__buttons">
      <button v-for="(tab, index) in tabs"
              class="tab__button"
              :key="index" @click="changeTab(index)"
              :class="{ 'tab__button_active': activeTab === index }">
        <span class="tab__button-text">
          {{ tab.label }}
        </span>
      </button>
    </div>
    <transition name="fade" mode="out-in">
      <div :key="activeTab" class="tab__content">
        <slot :name="tabs[activeTab].label"/>
      </div>
    </transition>
  </article>
</template>

<script setup>
const tabs = ref([
  { label: 'List' },
  { label: 'Activity' },
]);

const activeTab = ref(0);

const changeTab = (index) => {
  activeTab.value = index;
};
</script>

<style lang="scss">
 @import "styles.module";
</style>
