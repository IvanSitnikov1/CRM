<template>
    <article class="avatars">
        <div
            class="avatars__avatar"
            v-for="index in 3"
            :key="index"
            :class="{'avatars__avatar_last': index === 3}"
        >
            <img
                v-if="index < 3"
                src="@/shared/assets/test.png"
                alt="assigned"
                class="avatars__image-avatar"
            >
            <span v-else>
              +2
            </span>
        </div>
    </article>
</template>

<script setup lang="ts">
import { type ITag } from './../index'

const props = defineProps<{
  data: ITag
}>()

</script>

<style lang="scss">
 @import "styles.module";
</style>
