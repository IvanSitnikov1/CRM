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
              <IconBase :data="{
                iconName:  item.icon,
                iconColor: '#3F8CFF'
              }"/>
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
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";

const app = useAppModel()

const router = useRouter()
</script>


<style scoped lang="scss">
  @import "style.module";
</style>
