<template>
  <section class="wrapper wrapper_big info-panel__outer-wrapper">
    <article class="info-panel">
      <NavigationToggle />
      <div class="info-panel__panel">
        <div class="info-panel__search">
          <IconBase :data="{
            iconName: 'search'
          }"/>
        </div>
        <div class="info-panel__notification">
          <IconBase :data="{
            iconName: 'notification'
          }"/>
        </div>
        <div class="info-panel__profile" @click="handlerGoToProfile">
          <img src="./../../../shared/assets/test.png" alt="name" class="info-panel__profile-image">
        </div>
      </div>
    </article>
  </section>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { NavigationToggle } from '@/features/navigation'
import IconBase from "@/shared/ui/icon-base/ui/IconBase.vue";

const router = useRouter()

const handlerGoToProfile = () => {
  router.push({ path: '/profile' })
}

</script>


<style lang="scss">
  @import "style.module";
</style>
