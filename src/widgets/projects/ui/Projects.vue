<template>
  <div class="wrapper wrapper_big-margin">
    <section class="projects-container">
      <TitleWithLink :data="{
        title: {
          title: 'Projects'
        },
        link: {
          title: 'View all',
          to: '/projects'
        }
      }">
        <template #content>
            <section class="projects">
              <CardProject data=""/>
            </section>
        </template>
      </TitleWithLink>
    </section>
  </div>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { Card } from '@/entities/user'
import Link from '@/shared/ui/link/Link.vue'
import { TitleWithLink } from '@/entities/grop-title'
import CardProject from '@/entities/project/ui/card/CardProject.vue'

const router = useRouter()
const goToHome = () => {
  router.push({ path: '/' })
}

</script>


<style scoped lang="scss">
  @import "style.module";
</style>
