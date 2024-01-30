<template>
  <BottomSheet @onClose="app.updateShowFab(false)" :data="{
    open: app.showFab,
    title: 'Add..'
  }">
    <template #content>
      <section class="fab-content">
        <ul class="fab-content__list">
          <li v-for="(item, index) in fabConfig" :key="index" class="fab-content__element">
            <div class="fab-content__image-container">
              <img :src="getImageUrl(item.icon)" :alt="item.text">
            </div>
            <span class="fab-content__text">{{ item.text }}</span>
          </li>
        </ul>
      </section>
    </template>
  </BottomSheet>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { BottomSheet } from '@/entities/bottom-sheet'
import { useAppModel } from '@/entities/app'
import { fabConfig } from '@/widgets/fab'

const getImageUrl = (name) => {
  return new URL(`/src/shared/assets/icons/fab/${name}.svg`, import.meta.url).href
}
const app = useAppModel()

const router = useRouter()
const goToHome = () => {
  router.push({ path: '/' })
}

</script>


<style scoped lang="scss">
  @import "style.module";
</style>
