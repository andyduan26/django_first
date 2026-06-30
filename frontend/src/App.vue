<script setup>
import { computed, onMounted, onUnmounted, reactive, ref } from 'vue'
import { Heart, Search, ShoppingBag, Trash2, User, X } from '@lucide/vue'
import maisonNayaLogo from './assets/maison-naya-logo-transparent.png'

const routes = [
  { path: '/', label: 'Home', key: 'home' },
  { path: '/new-arrival', label: 'New Arrival', key: 'newArrival' },
  { path: '/bags', label: 'Bags', key: 'bags' },
  { path: '/jewellery', label: 'Jewellery', key: 'jewellery' },
  { path: '/contact-us', label: 'Contact us', key: 'contact' },
]

const arrivals = [
  {
    name: 'Noor Pearl Handle Bag',
    material: 'Cotton silk, pearls, Japanese beads',
    note: 'Pearl handle, satin lining, structured evening body',
    price: 'Wholesale enquiry',
    image:
      'https://img.perniaspopupshop.com/catalog/product/c/l/CLCH062402_1.jpg?impolicy=detailimageprod',
  },
  {
    name: 'Zari Bloom Beaded Clutch',
    material: 'Hand embroidery, sequins, faux suede lining',
    note: 'Soft floral surface for bridal and occasion edits',
    price: 'Made to order',
    image:
      'https://img.perniaspopupshop.com/catalog/product/d/o/DOXA052325_1.JPG?impolicy=detailimageprod',
  },
  {
    name: 'Asha Evening Minaudiere',
    material: 'Glass seed beads, metal frame, chain strap',
    note: 'Compact shape for private label gifting capsules',
    price: 'Private label ready',
    image:
      'https://img.perniaspopupshop.com/catalog/product/c/l/CLCH062402_1.jpg?impolicy=detailimageprod',
  },
]

const bagCategories = [
  {
    title: 'Pearl handle bags',
    body: 'Structured silhouettes with hand-wrapped pearl handles, smooth satin interiors, and export-ready dust bag packing.',
  },
  {
    title: 'Beaded box clutches',
    body: 'Architectural evening shapes with metal frames, crystal surfaces, clasp hardware, and optional shoulder chains.',
  },
  {
    title: 'Wedding potli bags',
    body: 'Soft drawstring bags for bridal parties, festive retail, destination weddings, and embellished gift assortments.',
  },
  {
    title: 'Resort mini bags',
    body: 'Lightweight beadwork, raffia trims, shell accents, and fresh colour stories for vacation and cruise edits.',
  },
  {
    title: 'Evening shoulder bags',
    body: 'Slim chain strap pieces with dense seed bead embroidery, suitable for occasionwear and department stores.',
  },
  {
    title: 'Private label capsules',
    body: 'Buyer-specific trims, label placement, barcode packing, carton planning, and repeated seasonal development.',
  },
]

const craftSteps = [
  'Sketch and sample',
  'Bead selection',
  'Hand embroidery',
  'Frame and lining',
  'Inspection',
  'Export packing',
]

const capabilities = [
  'Hand bead embroidery',
  'Pearl and crystal sourcing',
  'Colour card development',
  'Small batch sampling',
  'Private label packaging',
  'Export documentation support',
]

const jewellery = [
  {
    title: 'Beaded chokers',
    body: 'Pearl, crystal, and seed bead chokers developed to match bag embroidery or bridal colour stories.',
  },
  {
    title: 'Statement earrings',
    body: 'Lightweight occasion earrings with bead fringe, floral motifs, pearl drops, and retail-ready backing cards.',
  },
  {
    title: 'Pearl tassels',
    body: 'Soft tassel pieces for festive edits, bridesmaid gifting, and coordinated accessories capsules.',
  },
  {
    title: 'Occasion bracelets',
    body: 'Adjustable beaded bracelets designed for low-risk add-on sales and coordinated gift sets.',
  },
]

const qualityPoints = [
  'Bead density reviewed against approved sample',
  'Lining, handle, frame, and chain pull tested',
  'Dust bag, label, barcode, and carton sequence checked',
  'Final photos shared before dispatch when requested',
]

const contactForm = reactive({
  name: '',
  email: '',
  whatsapp: '',
  requirement: '',
})

const customerProfile = reactive({
  name: '',
  email: '',
  market: '',
})

const submitted = ref(false)
const submittedName = ref('')
const isSubmitting = ref(false)
const submitError = ref('')
const pathname = ref(window.location.pathname)
const activeUtilityPanel = ref('')
const searchQuery = ref('')
const likedProducts = ref(['Noor Pearl Handle Bag'])
const cartProducts = ref([])

const activeRoute = computed(() => {
  return routes.find((route) => route.path === pathname.value) ?? routes[0]
})

const searchableItems = computed(() => {
  return [
    ...arrivals.map((item) => ({
      title: item.name,
      category: 'New Arrival',
      body: `${item.material}. ${item.note}`,
      image: item.image,
      productName: item.name,
    })),
    ...bagCategories.map((item) => ({
      title: item.title,
      category: 'Bags',
      body: item.body,
      image: arrivals[0].image,
    })),
    ...jewellery.map((item) => ({
      title: item.title,
      category: 'Jewellery',
      body: item.body,
      image: arrivals[1].image,
    })),
  ]
})

const searchResults = computed(() => {
  const query = searchQuery.value.trim().toLowerCase()

  if (!query) {
    return searchableItems.value.slice(0, 5)
  }

  return searchableItems.value.filter((item) => {
    return `${item.title} ${item.category} ${item.body}`.toLowerCase().includes(query)
  })
})

const favoriteItems = computed(() => {
  return arrivals.filter((item) => likedProducts.value.includes(item.name))
})

const cartItems = computed(() => {
  return arrivals.filter((item) => cartProducts.value.includes(item.name))
})

function navigate(event, path) {
  event.preventDefault()
  if (window.location.pathname !== path) {
    window.history.pushState({}, '', path)
    pathname.value = path
    window.scrollTo({ top: 0 })
  }
}

function toggleUtilityPanel(panel) {
  activeUtilityPanel.value = activeUtilityPanel.value === panel ? '' : panel
}

function closeUtilityPanel() {
  activeUtilityPanel.value = ''
}

function addToFavorites(productName) {
  if (!likedProducts.value.includes(productName)) {
    likedProducts.value.push(productName)
  }
}

function removeFromFavorites(productName) {
  likedProducts.value = likedProducts.value.filter((item) => item !== productName)
}

function addToCart(productName) {
  if (!cartProducts.value.includes(productName)) {
    cartProducts.value.push(productName)
  }
}

function removeFromCart(productName) {
  cartProducts.value = cartProducts.value.filter((item) => item !== productName)
}

function isFavorite(productName) {
  return likedProducts.value.includes(productName)
}

function isInCart(productName) {
  return cartProducts.value.includes(productName)
}

async function submitContact() {
  submitted.value = false
  submitError.value = ''
  isSubmitting.value = true

  try {
    const response = await fetch('/api/contract/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name: contactForm.name,
        email: contactForm.email,
        whatsapp: contactForm.whatsapp,
        requirement: contactForm.requirement,
      }),
    })

    if (!response.ok) {
      throw new Error(`Contract API returned ${response.status}`)
    }

    const savedContract = await response.json()
    submittedName.value = savedContract.name
    submitted.value = true
    contactForm.name = ''
    contactForm.email = ''
    contactForm.whatsapp = ''
    contactForm.requirement = ''
  } catch (error) {
    submitError.value = 'Submission failed. Please check the server and try again.'
    console.warn('Could not submit contract form.', error)
  } finally {
    isSubmitting.value = false
  }
}

function syncPath() {
  pathname.value = window.location.pathname
}

onMounted(() => {
  window.addEventListener('popstate', syncPath)
})

onUnmounted(() => {
  window.removeEventListener('popstate', syncPath)
})
</script>

<template>
  <main class="site-shell">
    <header class="topbar">
      <a class="brand" href="/" aria-label="Maison Naya home" @click="navigate($event, '/')">
        <img class="brand-logo" :src="maisonNayaLogo" alt="Maison Naya" />
      </a>

      <div class="navigation-cluster">
        <nav class="nav-links" aria-label="Primary navigation">
          <a
            v-for="route in routes"
            :key="route.path"
            :class="{ active: activeRoute.path === route.path }"
            :href="route.path"
            @click="navigate($event, route.path)"
          >
            {{ route.label }}
          </a>
        </nav>

        <div class="utility-actions" aria-label="Shop tools">
          <button
            type="button"
            :class="{ active: activeUtilityPanel === 'search' }"
            aria-label="Search"
            title="Search"
            @click="toggleUtilityPanel('search')"
          >
            <Search :size="18" :stroke-width="1.6" />
          </button>
          <button
            type="button"
            :class="{ active: activeUtilityPanel === 'user' }"
            aria-label="User"
            title="User"
            @click="toggleUtilityPanel('user')"
          >
            <User :size="18" :stroke-width="1.6" />
          </button>
          <button
            type="button"
            :class="{ active: activeUtilityPanel === 'favorites' }"
            aria-label="Likes"
            title="Likes"
            @click="toggleUtilityPanel('favorites')"
          >
            <Heart :size="18" :stroke-width="1.6" />
            <span v-if="favoriteItems.length">{{ favoriteItems.length }}</span>
          </button>
          <button
            type="button"
            :class="{ active: activeUtilityPanel === 'cart' }"
            aria-label="Cart"
            title="Cart"
            @click="toggleUtilityPanel('cart')"
          >
            <ShoppingBag :size="18" :stroke-width="1.6" />
            <span v-if="cartItems.length">{{ cartItems.length }}</span>
          </button>
        </div>
      </div>
    </header>

    <section v-if="activeUtilityPanel" class="utility-panel" aria-label="Selected shop tool">
      <div class="utility-panel-head">
        <div>
          <p class="eyebrow">
            {{
              {
                search: 'Search',
                user: 'User',
                favorites: 'Likes',
                cart: 'Cart',
              }[activeUtilityPanel]
            }}
          </p>
          <h2>
            {{
              {
                search: 'Find beaded bags and accessories.',
                user: 'Save buyer details for enquiries.',
                favorites: 'Review your selected favourites.',
                cart: 'Prepare an enquiry basket.',
              }[activeUtilityPanel]
            }}
          </h2>
        </div>
        <button type="button" aria-label="Close panel" title="Close" @click="closeUtilityPanel">
          <X :size="20" :stroke-width="1.6" />
        </button>
      </div>

      <div v-if="activeUtilityPanel === 'search'" class="search-module">
        <label>
          Search collection
          <input v-model="searchQuery" type="search" placeholder="Pearl clutch, potli, earrings..." />
        </label>
        <div class="module-list">
          <article v-for="item in searchResults" :key="`${item.category}-${item.title}`">
            <img :src="item.image" :alt="item.title" />
            <div>
              <small>{{ item.category }}</small>
              <h3>{{ item.title }}</h3>
              <p>{{ item.body }}</p>
              <button
                v-if="item.productName"
                type="button"
                @click="addToFavorites(item.productName)"
              >
                Add to likes
              </button>
            </div>
          </article>
        </div>
      </div>

      <form v-else-if="activeUtilityPanel === 'user'" class="user-module">
        <label>
          Name
          <input v-model="customerProfile.name" type="text" placeholder="Buyer name" />
        </label>
        <label>
          Email
          <input v-model="customerProfile.email" type="email" placeholder="buyer@example.com" />
        </label>
        <label>
          Market
          <input v-model="customerProfile.market" type="text" placeholder="USA, Europe, Middle East..." />
        </label>
        <p>
          These details stay in this front-end session and help you prepare a cleaner enquiry before
          sending the contact form.
        </p>
      </form>

      <div v-else-if="activeUtilityPanel === 'favorites'" class="module-list">
        <article v-if="!favoriteItems.length" class="empty-module">
          <div>
            <h3>No liked products yet.</h3>
            <p>Use the heart action on new arrivals to build a focused reference list.</p>
          </div>
        </article>
        <template v-else>
          <article v-for="item in favoriteItems" :key="item.name">
            <img :src="item.image" :alt="item.name" />
            <div>
              <small>Liked product</small>
              <h3>{{ item.name }}</h3>
              <p>{{ item.note }}</p>
              <div class="module-actions">
                <button type="button" @click="addToCart(item.name)">Add to cart</button>
                <button type="button" aria-label="Remove like" @click="removeFromFavorites(item.name)">
                  <Trash2 :size="16" :stroke-width="1.6" />
                </button>
              </div>
            </div>
          </article>
        </template>
      </div>

      <div v-else class="module-list">
        <article v-if="!cartItems.length" class="empty-module">
          <div>
            <h3>Your enquiry cart is empty.</h3>
            <p>Add styles from new arrivals, then send the selection through the contact page.</p>
          </div>
        </article>
        <template v-else>
          <article v-for="item in cartItems" :key="item.name">
            <img :src="item.image" :alt="item.name" />
            <div>
              <small>Enquiry cart</small>
              <h3>{{ item.name }}</h3>
              <p>{{ item.material }}</p>
              <div class="module-actions">
                <a href="/contact-us" @click="navigate($event, '/contact-us')">Enquire now</a>
                <button type="button" aria-label="Remove from cart" @click="removeFromCart(item.name)">
                  <Trash2 :size="16" :stroke-width="1.6" />
                </button>
              </div>
            </div>
          </article>
        </template>
      </div>
    </section>

    <template v-if="activeRoute.key === 'home'">
      <section class="hero">
        <div class="hero-copy">
          <p class="eyebrow">Source from India</p>
          <h1>Hand beaded bags for refined occasion brands.</h1>
          <p class="lede">
            Maison Naya works with Indian artisan clusters to develop pearl, seed bead, crystal,
            and sequined evening bags for boutiques, designers, bridal labels, and private label buyers.
          </p>
          <div class="hero-actions">
            <a class="button primary" href="/new-arrival" @click="navigate($event, '/new-arrival')">
              View new arrivals
            </a>
            <a class="button secondary" href="/contact-us" @click="navigate($event, '/contact-us')">
              Request catalogue
            </a>
          </div>
        </div>

        <div class="hero-media" aria-label="Hand beaded pearl bag">
          <img :src="arrivals[0].image" alt="Pearl and bead embellished handmade evening bag" />
          <div class="media-note">
            <span>Lead time</span>
            <strong>3-5 weeks</strong>
          </div>
        </div>
      </section>

      <section class="signature-strip" aria-label="Company highlights">
        <div>
          <strong>India origin</strong>
          <span>Jaipur, Delhi NCR, Mumbai partner workshops</span>
        </div>
        <div>
          <strong>Small MOQ</strong>
          <span>Buyer-friendly sampling and capsule orders</span>
        </div>
        <div>
          <strong>Export ready</strong>
          <span>Quality control, dust bags, barcode packing</span>
        </div>
      </section>

      <section class="section two-column">
        <div>
          <p class="eyebrow">Atelier network</p>
          <h2>Quiet luxury, made by patient hands.</h2>
        </div>
        <div class="prose">
          <p>
            Our sourcing network is built around specialist Indian handwork units rather than mass
            accessory lines. That means controlled sampling, closer bead matching, and a slower visual
            language suited to premium occasion retail.
          </p>
          <p>
            We support founders, buying offices, and designers who want beadwork to feel considered:
            clean silhouettes, fine surfaces, restrained hardware, and packaging that looks composed
            before the product reaches the shelf.
          </p>
        </div>
      </section>

      <section class="section">
        <div class="section-heading">
          <div>
            <p class="eyebrow">What we supply</p>
            <h2>Commercial pieces with a hand-finished point of view.</h2>
          </div>
          <p>
            Bags, jewellery, and coordinated small capsules are developed for wholesale, private label,
            gifting, bridal, and resort assortments.
          </p>
        </div>
        <div class="text-grid">
          <article v-for="item in capabilities" :key="item">
            <span></span>
            <h3>{{ item }}</h3>
          </article>
        </div>
      </section>
    </template>

    <template v-else-if="activeRoute.key === 'newArrival'">
      <section class="page-hero">
        <p class="eyebrow">New Arrival</p>
        <h1>Fresh beadwork stories for evening and bridal collections.</h1>
        <p class="lede">
          A focused edit of hand finished styles: pearl-dense surfaces, dimensional floral beadwork,
          polished handles, and soft satin interiors.
        </p>
      </section>

      <section class="section">
        <div class="product-grid">
          <article v-for="item in arrivals" :key="item.name" class="product-card">
            <img :src="item.image" :alt="item.name" />
            <div>
              <h3>{{ item.name }}</h3>
              <p>{{ item.material }}</p>
              <small>{{ item.note }}</small>
              <span>{{ item.price }}</span>
              <div class="product-actions">
                <button
                  type="button"
                  :class="{ selected: isFavorite(item.name) }"
                  @click="addToFavorites(item.name)"
                >
                  <Heart :size="16" :stroke-width="1.6" />
                  {{ isFavorite(item.name) ? 'Liked' : 'Like' }}
                </button>
                <button
                  type="button"
                  :class="{ selected: isInCart(item.name) }"
                  @click="addToCart(item.name)"
                >
                  <ShoppingBag :size="16" :stroke-width="1.6" />
                  {{ isInCart(item.name) ? 'In cart' : 'Cart' }}
                </button>
              </div>
            </div>
          </article>
        </div>
      </section>

      <section class="section editorial-row">
        <div>
          <p class="eyebrow">Season notes</p>
          <h2>Pearl surfaces, fine florals, and warm neutral metallics.</h2>
        </div>
        <div class="prose">
          <p>
            The new arrival direction is built for refined occasionwear buyers: ivory pearl fields,
            champagne trims, soft gold hardware, muted florals, and compact shapes that photograph well
            without feeling theatrical.
          </p>
          <p>
            Each design can be sampled as a finished style or adapted into an exclusive colour story
            for your market.
          </p>
        </div>
      </section>

      <section class="section">
        <div class="text-grid">
          <article>
            <span></span>
            <h3>Sample route</h3>
            <p>Choose from the new arrival edit, then adjust bead colours, lining, and hardware finish.</p>
          </article>
          <article>
            <span></span>
            <h3>Buyer review</h3>
            <p>Receive close-up photos, dimensions, material notes, and packaging suggestions.</p>
          </article>
          <article>
            <span></span>
            <h3>Order planning</h3>
            <p>Confirm quantities, delivery windows, labelling, and carton-level packing requirements.</p>
          </article>
        </div>
      </section>
    </template>

    <template v-else-if="activeRoute.key === 'bags'">
      <section class="page-hero">
        <p class="eyebrow">Bags</p>
        <h1>From occasion clutches to private label capsules.</h1>
        <p class="lede">
          We develop structured evening silhouettes with hand-applied beads, pearls, crystals,
          raffia accents, satin linings, chain straps, and custom trims.
        </p>
      </section>

      <section class="section">
        <div class="category-list">
          <article v-for="category in bagCategories" :key="category.title">
            <span></span>
            <div>
              <h3>{{ category.title }}</h3>
              <p>{{ category.body }}</p>
            </div>
          </article>
        </div>
      </section>

      <section class="craft-section">
        <div class="section-heading narrow">
          <p class="eyebrow">Workshop process</p>
          <h2>Measured development, hand finished detail.</h2>
        </div>
        <div class="process-grid">
          <article v-for="(step, index) in craftSteps" :key="step">
            <span>{{ String(index + 1).padStart(2, '0') }}</span>
            <h3>{{ step }}</h3>
          </article>
        </div>
      </section>

      <section class="section two-column">
        <div>
          <p class="eyebrow">Customization</p>
          <h2>Built around the buyer brief.</h2>
        </div>
        <div class="prose">
          <p>
            We can adapt bead density, handle shape, chain length, lining colour, closure type,
            dust bag fabric, swing tag, barcode sticker, and carton marking according to your retail plan.
          </p>
          <p>
            For private label work, design confidentiality and repeatable production notes are maintained
            from sample approval through final packing.
          </p>
        </div>
      </section>
    </template>

    <template v-else-if="activeRoute.key === 'jewellery'">
      <section class="page-hero">
        <p class="eyebrow">Jewellery</p>
        <h1>Complementary bead and pearl accessories.</h1>
        <p class="lede">
          Capsule add-ons for retail sets: chokers, earrings, pearl tassels, and occasion bracelets
          designed to sit naturally beside embellished clutches.
        </p>
      </section>

      <section class="section jewellery-section">
        <div>
          <p class="eyebrow">Accessory desk</p>
          <h2>Designed for colour matching and assortment planning.</h2>
          <p>
            Jewellery samples can be developed alongside bag capsules for cohesive bridal,
            occasion, and resort edits.
          </p>
        </div>

        <div class="jewellery-grid">
          <article v-for="item in jewellery" :key="item.title">
            <h3>{{ item.title }}</h3>
            <p>{{ item.body }}</p>
          </article>
        </div>
      </section>

      <section class="section editorial-row">
        <div>
          <p class="eyebrow">Merchandising</p>
          <h2>Small accessories that complete the display.</h2>
        </div>
        <div class="prose">
          <p>
            Jewellery is planned as a soft extension of the bag range, not as a separate visual language.
            Pearl tones, metal finishes, bead sizes, and packaging papers can be aligned so the collection
            presents as one refined story.
          </p>
          <p>
            This is useful for bridal retail, resort stores, curated gift edits, and compact online drops.
          </p>
        </div>
      </section>

      <section class="section">
        <div class="text-grid">
          <article>
            <span></span>
            <h3>Matching service</h3>
            <p>Coordinate jewellery bead colours with approved bag samples or seasonal palette cards.</p>
          </article>
          <article>
            <span></span>
            <h3>Retail packaging</h3>
            <p>Backing cards, pouches, labels, and barcode stickers can be planned with the buyer.</p>
          </article>
          <article>
            <span></span>
            <h3>Capsule quantities</h3>
            <p>Develop low-risk add-on assortments beside the core bag order.</p>
          </article>
        </div>
      </section>
    </template>

    <template v-else>
      <section class="page-hero">
        <p class="eyebrow">Contact us</p>
        <h1>Build your next beaded accessories range at source.</h1>
        <p class="lede">
          Share your target market, desired silhouettes, quantity range, and delivery window.
          We will prepare a focused proposal with sample options and production notes.
        </p>
      </section>

      <section class="section contact-section">
        <div>
          <p class="eyebrow">Buyer enquiries</p>
          <h2>Sampling, private label, and wholesale production.</h2>
          <p>
            Tell us the collection mood, material direction, target price range, and shipment month.
            Our team will respond with a practical development route.
          </p>
          <div class="contact-details">
            <article>
              <strong>Email</strong>
              <span>sourcing@maisonnaya.example</span>
            </article>
            <article>
              <strong>WhatsApp</strong>
              <span>+91 00000 00000</span>
            </article>
            <article>
              <strong>Focus</strong>
              <span>Hand beaded bags, jewellery, private label capsules</span>
            </article>
          </div>
        </div>

        <form class="contact-card" aria-label="Catalogue request form" @submit.prevent="submitContact">
          <label>
            Name
            <input v-model="contactForm.name" type="text" placeholder="Your name" required />
          </label>
          <label>
            Email
            <input v-model="contactForm.email" type="email" placeholder="buyer@example.com" required />
          </label>
          <label>
            WhatsApp
            <input v-model="contactForm.whatsapp" type="tel" placeholder="+86 / +91 / +1 ..." required />
          </label>
          <label>
            Requirement
            <textarea
              v-model="contactForm.requirement"
              placeholder="Tell us about your collection, quantity, market, and timeline"
              required
            ></textarea>
          </label>
          <button type="submit" :disabled="isSubmitting">
            {{ isSubmitting ? 'Submitting...' : 'Submit enquiry' }}
          </button>
          <p v-if="submitted" class="form-success">
            Thank you, {{ submittedName }}. Your enquiry has been saved.
          </p>
          <p v-if="submitError" class="form-error">
            {{ submitError }}
          </p>
        </form>
      </section>

      <section class="section">
        <div class="section-heading">
          <div>
            <p class="eyebrow">Before you write</p>
            <h2>Helpful details for a precise quotation.</h2>
          </div>
          <p>
            A clear first message helps us answer with suitable materials, sampling route, and realistic
            delivery timing.
          </p>
        </div>
        <div class="text-grid">
          <article>
            <span></span>
            <h3>Product direction</h3>
            <p>Share silhouettes, bead mood, colour palette, and any reference target.</p>
          </article>
          <article>
            <span></span>
            <h3>Quantity range</h3>
            <p>Mention whether you need samples, a capsule order, or repeated wholesale production.</p>
          </article>
          <article>
            <span></span>
            <h3>Market and timing</h3>
            <p>Tell us your destination market, price level, launch month, and packaging needs.</p>
          </article>
        </div>
      </section>
    </template>

    <footer class="footer">
      <span>Maison Naya</span>
      <span>Indian source hand beaded bags and jewellery</span>
    </footer>
  </main>
</template>
