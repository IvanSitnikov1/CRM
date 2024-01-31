<template>
  <PopUp @onClose="closeSupport" :data="{
    title: 'Need some Help?',
    open: app.showSupport
  }">
    <template #content>
      <div class="support">
        <p class="support__text">
          Describe your question and our specialists will answer you within 24 hours.
        </p>
      </div>
    </template>
  </PopUp>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
const router = useRouter()

import { useAppModel } from '@/entities/app'
import { PopUp } from '@/entities/popup'

const app = useAppModel()


const closeSupport = () => {
  app.updateShowSupport(false)
};
</script>


<style lang="scss">
  @import "style.module";


</style>
