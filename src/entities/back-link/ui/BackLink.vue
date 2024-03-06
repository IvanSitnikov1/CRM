<template>
    <div class="wrapper wrapper_title">
        <Link
            :data="{
                title: `Back to ${getParentPath}`,
                to: `/${getParentPath}`,
                iconLeft: 'arrowLeftLong',
            }"
        />
    </div>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router';
import { Link } from '@/shared/ui/link';

const route = useRoute();
const getParentPath = computed(() => {
  const pathSegments = route.path.split('/');
  const goToRoot = pathSegments.length === 2;
  return goToRoot ? pathSegments[0] : pathSegments[1];
});
</script>
