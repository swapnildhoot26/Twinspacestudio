(() => {
  'use strict';

  const body = document.body;
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const localImage = (uuid) => `assets/images/external/${uuid}.jpg`;

  const projectDialogs = [...document.querySelectorAll('[data-project-dialog]')];
  const storyDialog = document.querySelector('[data-story-dialog]');
  const lightbox = document.querySelector('[data-lightbox]');
  let activeDialog = null;
  let returnFocus = null;
  let gallery = [];
  let galleryIndex = 0;

  function openDialog(dialog, trigger) {
    if (!dialog) return;
    returnFocus = trigger || document.activeElement;
    activeDialog = dialog;
    dialog.hidden = false;
    body.classList.add('modal-open');
    dialog.scrollTop = 0;
    dialog.querySelector('button, a')?.focus({ preventScroll: true });
  }

  function closeDialog(dialog, restoreFocus = true) {
    if (!dialog) return;
    dialog.hidden = true;
    if (activeDialog === dialog) activeDialog = null;
    if (!activeDialog && (!lightbox || lightbox.hidden)) body.classList.remove('modal-open');
    if (restoreFocus) returnFocus?.focus?.({ preventScroll: true });
  }

  document.querySelectorAll('[data-open-project]').forEach((card) => {
    const open = () => openDialog(projectDialogs[Number(card.dataset.openProject)], card);
    card.addEventListener('click', open);
    if (card.tagName !== 'BUTTON') {
      card.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          open();
        }
      });
    }
  });

  projectDialogs.forEach((dialog, index) => {
    dialog.querySelector('[data-close-project]')?.addEventListener('click', () => closeDialog(dialog));
    dialog.querySelector('[data-next-project]')?.addEventListener('click', () => {
      closeDialog(dialog, false);
      openDialog(projectDialogs[(index + 1) % projectDialogs.length], returnFocus);
    });
    dialog.querySelectorAll('figure [role="button"]').forEach((button, itemIndex) => {
      const open = () => openLightbox(dialog, itemIndex, button);
      button.addEventListener('click', open);
      button.addEventListener('keydown', (event) => {
        if (event.key === 'Enter' || event.key === ' ') {
          event.preventDefault();
          open();
        }
      });
    });
  });

  document.querySelector('[data-open-story]')?.addEventListener('click', (event) => {
    event.preventDefault();
    openDialog(storyDialog, event.currentTarget);
  });
  storyDialog?.querySelectorAll('[data-close-story]').forEach((button) => {
    button.addEventListener('click', () => closeDialog(storyDialog));
  });

  function galleryItems(dialog) {
    return [...dialog.querySelectorAll('figure [role="button"]')].map((button) => {
      const image = button.querySelector('img');
      return { src: image?.getAttribute('src') || '', alt: image?.getAttribute('alt') || button.getAttribute('aria-label') || '' };
    });
  }

  function renderLightbox() {
    if (!lightbox || !gallery.length) return;
    const item = gallery[galleryIndex];
    const image = lightbox.querySelector('[data-lightbox-image]');
    const caption = lightbox.querySelector('[data-lightbox-caption]');
    const count = [...lightbox.querySelectorAll('p')].find((node) => /^\d+\s*\/\s*\d+$/.test(node.textContent.trim()));
    if (image) {
      image.style.backgroundImage = `url("${item.src}")`;
      image.setAttribute('aria-label', item.alt);
    }
    if (caption) caption.textContent = item.alt;
    if (count) count.textContent = `${galleryIndex + 1} / ${gallery.length}`;

    const row = lightbox.querySelector('[data-lightbox-thumbnails]');
    if (row) {
      row.replaceChildren(...gallery.map((entry, index) => {
        const button = document.createElement('button');
        button.type = 'button';
        button.setAttribute('aria-label', entry.alt);
        button.style.cssText = `flex:none;width:74px;height:56px;padding:0;background:none;cursor:pointer;opacity:${index === galleryIndex ? 1 : 0.45};border:1px solid ${index === galleryIndex ? '#D8B884' : 'rgba(245,240,232,.22)'}`;
        const imageElement = document.createElement('img');
        imageElement.src = entry.src;
        imageElement.alt = '';
        imageElement.loading = 'lazy';
        imageElement.style.cssText = 'width:100%;height:100%;object-fit:cover;display:block';
        button.append(imageElement);
        button.addEventListener('click', () => {
          galleryIndex = index;
          renderLightbox();
        });
        return button;
      }));
    }
  }

  function openLightbox(dialog, index, trigger) {
    if (!lightbox) return;
    gallery = galleryItems(dialog);
    galleryIndex = index;
    returnFocus = trigger;
    lightbox.hidden = false;
    body.classList.add('modal-open');
    renderLightbox();
    lightbox.querySelector('[data-close-lightbox]')?.focus({ preventScroll: true });
  }

  function closeLightbox() {
    if (!lightbox) return;
    lightbox.hidden = true;
    if (!activeDialog) body.classList.remove('modal-open');
    returnFocus?.focus?.({ preventScroll: true });
  }

  lightbox?.querySelector('[data-close-lightbox]')?.addEventListener('click', closeLightbox);
  lightbox?.querySelector('[data-previous-image]')?.addEventListener('click', () => {
    galleryIndex = (galleryIndex - 1 + gallery.length) % gallery.length;
    renderLightbox();
  });
  lightbox?.querySelector('[data-next-image]')?.addEventListener('click', () => {
    galleryIndex = (galleryIndex + 1) % gallery.length;
    renderLightbox();
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      if (lightbox && !lightbox.hidden) closeLightbox();
      else if (activeDialog) closeDialog(activeDialog);
      else if (body.classList.contains('menu-open')) toggleMenu(false);
    } else if (lightbox && !lightbox.hidden && event.key === 'ArrowLeft') {
      galleryIndex = (galleryIndex - 1 + gallery.length) % gallery.length;
      renderLightbox();
    } else if (lightbox && !lightbox.hidden && event.key === 'ArrowRight') {
      galleryIndex = (galleryIndex + 1) % gallery.length;
      renderLightbox();
    }
  });

  const nav = document.querySelector('[data-nav]');
  const navToggle = nav?.querySelector('[data-navtoggle]');
  const mobileMenu = document.querySelector('[data-mobile-menu]');
  let lastScrollY = window.scrollY;

  function toggleMenu(force) {
    const open = typeof force === 'boolean' ? force : !body.classList.contains('menu-open');
    body.classList.toggle('menu-open', open);
    navToggle?.setAttribute('aria-expanded', String(open));
    if (mobileMenu) mobileMenu.hidden = !open;
  }
  navToggle?.addEventListener('click', () => toggleMenu());
  nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => toggleMenu(false)));
  mobileMenu?.querySelector('[data-close-menu]')?.addEventListener('click', () => toggleMenu(false));
  mobileMenu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => toggleMenu(false)));

  function updateNavigation() {
    if (!nav) return;
    const y = window.scrollY;
    const solid = y > 90;
    const difference = y - lastScrollY;
    if (Math.abs(difference) > 4) {
      nav.style.transform = difference > 0 && y > 160 && !body.classList.contains('menu-open') ? 'translateY(-118%)' : 'translateY(0)';
      lastScrollY = y;
    }
    nav.style.background = solid ? 'rgba(245,240,232,.94)' : 'rgba(42,36,30,0)';
    nav.style.borderBottomColor = solid ? 'rgba(42,36,30,.12)' : 'rgba(42,36,30,0)';
    nav.style.padding = solid ? '12px clamp(18px,4vw,54px)' : '18px clamp(18px,4vw,54px)';
    const ink = solid ? '#2A241E' : '#F5F0E8';
    nav.querySelectorAll('[data-navink]').forEach((link) => {
      link.style.color = ink;
      link.style.textShadow = solid ? 'none' : '0 1px 10px rgba(28,24,20,.55)';
    });
    if (navToggle) navToggle.style.color = ink;
    const logo = nav.querySelector('[data-navlogo]');
    if (logo) logo.src = solid ? 'assets/images/logo-mark.png' : 'assets/images/logo-mark-light.png';
    const pill = nav.querySelector('[data-navpill]');
    if (pill) {
      pill.style.background = solid ? '#B08D57' : 'transparent';
      pill.style.borderColor = solid ? '#B08D57' : 'rgba(245,240,232,.45)';
      pill.style.color = solid ? '#fff' : '#F5F0E8';
      pill.style.boxShadow = solid ? '0 6px 18px rgba(42,36,30,.18)' : 'none';
    }
    const parallax = document.querySelector('[data-parallax]');
    if (parallax && !reduceMotion) parallax.style.transform = `translate3d(0,${Math.min(y * 0.16, 170)}px,0)`;
  }
  window.addEventListener('scroll', updateNavigation, { passive: true });
  updateNavigation();

  const heroSlides = [...document.querySelectorAll('[data-heroimg]')];
  const heroDots = [...document.querySelectorAll('[data-herodots] button')];
  const mobileHero = window.matchMedia('(max-width: 699px)');
  let heroIndex = 0;
  function renderHero(index) {
    heroIndex = index;
    heroSlides.forEach((slide, itemIndex) => {
      const source = mobileHero.matches ? slide.dataset.heroMobileSrc : slide.dataset.heroSrc;
      if (itemIndex === index && source && slide.dataset.loadedHero !== source) {
        slide.style.backgroundImage = `url("${source}")`;
        slide.dataset.loadedHero = source;
      }
      slide.style.opacity = itemIndex === index ? '1' : '0';
      slide.style.transform = itemIndex === index ? 'scale(1)' : 'scale(1.08)';
    });
    heroDots.forEach((dot, itemIndex) => {
      const line = dot.firstElementChild || dot;
      line.style.width = itemIndex === index ? '26px' : '10px';
      line.style.background = itemIndex === index ? '#D8B884' : 'rgba(245,240,232,.45)';
    });
  }
  heroDots.forEach((dot, index) => dot.addEventListener('click', () => renderHero(index)));
  mobileHero.addEventListener('change', () => renderHero(heroIndex));
  if (heroSlides.length) renderHero(0);
  if (!reduceMotion && heroSlides.length) {
    window.setInterval(() => renderHero((heroIndex + 1) % heroSlides.length), 6760);
  }

  const hero = document.querySelector('[data-hero]');
  const glow = document.querySelector('[data-heroglow]');
  if (hero && glow && !reduceMotion && window.matchMedia('(hover:hover)').matches) {
    hero.addEventListener('pointermove', (event) => {
      const bounds = hero.getBoundingClientRect();
      glow.style.opacity = '1';
      glow.style.transform = `translate3d(${event.clientX - bounds.left - 260}px,${event.clientY - bounds.top - 260}px,0)`;
    });
    hero.addEventListener('pointerleave', () => { glow.style.opacity = '0'; });
  }

  const testimonials = [
    {
      heading: 'Spaces that make a difference.',
      text: 'They understood what we wanted before we could explain it. Every drawing came back closer to the home we had in our heads.',
      name: 'Aniket & Pooja', location: '4 BHK, Koregaon Park',
      image: localImage('c724a564-0656-4a4c-9467-b3e123e8f91a'), face: localImage('725d17f9-65a1-4bea-9ec9-748e2066bccb')
    },
    {
      heading: 'A home that works at 5am.',
      text: 'I work nights, so they designed the whole flat around one person moving quietly at 5am — and it works exactly like that, every single shift.',
      name: 'Dr. Meera S.', location: '3 BHK, Kothrud',
      image: localImage('5614cf90-4325-48c2-ba7a-3afe47611fb4'), face: localImage('0a4358de-be3b-40b7-b53c-53215ecd2d2e')
    },
    {
      heading: 'Not one rupee of surprise.',
      text: 'Quote on day one, the same number on handover day, and a dated plan we could hold them to. As a founder myself, that is what I still talk about.',
      name: 'Karthik R.', location: 'Villa, Baner',
      image: localImage('6016ad09-8a11-483e-a18e-319237c8c6db'), face: localImage('508602b4-eeb0-4882-9643-30479f059948')
    }
  ];
  const testimonialRoot = document.querySelector('[data-testimonials]');
  let testimonialIndex = 0;
  function renderTestimonial(index) {
    if (!testimonialRoot) return;
    testimonialIndex = (index + testimonials.length) % testimonials.length;
    const item = testimonials[testimonialIndex];
    testimonialRoot.querySelector('[data-testimonial-heading]').textContent = item.heading;
    testimonialRoot.querySelector('[data-testimonial-quote]').textContent = `“${item.text}”`;
    testimonialRoot.querySelector('[data-testimonial-name]').textContent = item.name;
    testimonialRoot.querySelector('[data-testimonial-location]').textContent = item.location;
    testimonialRoot.querySelector('[data-testimonial-image]').style.backgroundImage = `url("${item.image}")`;
    testimonialRoot.querySelector('[data-testimonial-image]').setAttribute('aria-label', `Home of ${item.name}`);
    testimonialRoot.querySelector('[data-testimonial-face]').style.backgroundImage = `url("${item.face}")`;
    testimonialRoot.querySelectorAll('[data-testimonial-dot]').forEach((dot, dotIndex) => {
      const line = dot.firstElementChild || dot;
      line.style.width = dotIndex === testimonialIndex ? '20px' : '10px';
      line.style.background = dotIndex === testimonialIndex ? '#B08D57' : 'rgba(42,36,30,.28)';
    });
  }
  testimonialRoot?.querySelectorAll('[data-testimonial-dot]').forEach((dot, index) => dot.addEventListener('click', () => renderTestimonial(index)));
  testimonialRoot?.querySelector('[aria-label="Previous testimonial"]')?.addEventListener('click', () => renderTestimonial(testimonialIndex - 1));
  testimonialRoot?.querySelector('[aria-label="Next testimonial"]')?.addEventListener('click', () => renderTestimonial(testimonialIndex + 1));

  function initWebGL(canvas) {
    const gl = canvas.getContext('webgl', { alpha: true, premultipliedAlpha: true, antialias: false });
    if (!gl) return;
    const vertex = 'attribute vec2 p; void main(){ gl_Position = vec4(p,0.0,1.0); }';
    const fragment = [
      'precision mediump float;',
      'uniform vec2 u_res; uniform float u_t; uniform vec2 u_m;',
      'float hash(vec2 p){ return fract(sin(dot(p, vec2(127.1,311.7))) * 43758.5453); }',
      'void main(){ vec2 uv=gl_FragCoord.xy/u_res; float diag=uv.x*.6+(1.0-uv.y)*.6;',
      'float centre=.34+.24*sin(u_t*.12)+.05*u_m.x; float beam=smoothstep(.28,0.0,abs(diag-centre))*.4;',
      'vec2 warm=vec2(.72+.05*u_m.x,.66+.05*u_m.y); float haze=smoothstep(.8,.05,length((uv-warm)*vec2(1.0,.78)))*.24;',
      'float grain=(hash(gl_FragCoord.xy+floor(u_t*8.0))-.5)*.03; float a=clamp(beam+haze+grain,0.0,1.0);',
      'vec3 col=mix(vec3(.98,.94,.86),vec3(.78,.62,.38),haze*3.0); gl_FragColor=vec4(col*a,a); }'
    ].join('\n');
    const shader = (type, source) => { const value = gl.createShader(type); gl.shaderSource(value, source); gl.compileShader(value); return value; };
    const program = gl.createProgram();
    gl.attachShader(program, shader(gl.VERTEX_SHADER, vertex));
    gl.attachShader(program, shader(gl.FRAGMENT_SHADER, fragment));
    gl.linkProgram(program);
    if (!gl.getProgramParameter(program, gl.LINK_STATUS)) return;
    gl.useProgram(program);
    const buffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    const location = gl.getAttribLocation(program, 'p');
    gl.enableVertexAttribArray(location);
    gl.vertexAttribPointer(location, 2, gl.FLOAT, false, 0, 0);
    const resolution = gl.getUniformLocation(program, 'u_res');
    const time = gl.getUniformLocation(program, 'u_t');
    const mouseUniform = gl.getUniformLocation(program, 'u_m');
    const mouse = [0, 0];
    const mouseTarget = [0, 0];
    const ratio = Math.min(window.devicePixelRatio || 1, 1.5);
    const resize = () => {
      const bounds = canvas.getBoundingClientRect();
      canvas.width = Math.max(2, Math.round(bounds.width * ratio));
      canvas.height = Math.max(2, Math.round(bounds.height * ratio));
      gl.viewport(0, 0, canvas.width, canvas.height);
    };
    resize();
    window.addEventListener('resize', resize);
    if (!reduceMotion) window.addEventListener('pointermove', (event) => {
      const bounds = canvas.getBoundingClientRect();
      mouseTarget[0] = ((event.clientX - bounds.left) / bounds.width) * 2 - 1;
      mouseTarget[1] = ((event.clientY - bounds.top) / bounds.height) * 2 - 1;
    }, { passive: true });
    const started = performance.now();
    function frame() {
      mouse[0] += (mouseTarget[0] - mouse[0]) * 0.045;
      mouse[1] += (mouseTarget[1] - mouse[1]) * 0.045;
      gl.uniform2f(resolution, canvas.width, canvas.height);
      gl.uniform1f(time, reduceMotion ? 6 : (performance.now() - started) / 1000);
      gl.uniform2f(mouseUniform, mouse[0], mouse[1]);
      gl.drawArrays(gl.TRIANGLES, 0, 3);
      requestAnimationFrame(frame);
    }
    frame();
  }
  const canvas = document.querySelector('[data-gl]');
  if (canvas && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      if (!entries.some((entry) => entry.isIntersecting)) return;
      observer.disconnect();
      initWebGL(canvas);
    }, { rootMargin: '180px' });
    observer.observe(canvas);
  } else if (canvas) {
    window.setTimeout(() => initWebGL(canvas), 1_000);
  }
})();
