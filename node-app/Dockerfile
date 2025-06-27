FROM node:22-alpine

# Set working directory
WORKDIR /usr/src/app

# Install dependencies separately for caching
COPY package*.json ./
RUN npm install --omit=dev

# Copy app files
COPY . .

# Expose port
EXPOSE 3000

# Start the app
CMD ["npm", "start"]
